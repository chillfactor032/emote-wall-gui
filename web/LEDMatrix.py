import os
import time
import threading
import numpy as np
from PIL import Image, ImageEnhance 
import adafruit_blinka_raspberry_pi5_piomatter as piomatter

class Matrix():

    def __init__(self, width, height, **kwargs):
        self.width = width
        self.height = height
        self._brightness = min(1.0, kwargs.get("brightness", 0.5))
        self._pinout = kwargs.get("pinout", piomatter.Pinout.AdafruitMatrixBonnet)
        self._n_address_lines = kwargs.get("n_addr_lines", 4)
        self._geometry = kwargs.get("geometry", piomatter.Geometry(
            width=width, 
            height=height, 
            n_addr_lines=self._n_address_lines,
            rotation=piomatter.Orientation.Normal))
        self._blank_img = Image.new("RGB", (width, height))
        self._framebuffer = np.asarray(self._blank_img) + 0 
        self._colorspace = kwargs.get("colorspace", piomatter.Colorspace.RGB888Packed)
        self._matrix = piomatter.PioMatter(
            colorspace=self._colorspace,
            pinout=self._pinout,
            framebuffer=self._framebuffer,
            geometry=self._geometry)
        self._gif_thread = None
        self._gif_stop_event = threading.Event()
    
    def _update_framebuffer(self, framedata):
        """Write frame data to the buffer and refresh the matrix"""
        enhancer = ImageEnhance.Brightness(framedata)
        framedata = enhancer.enhance(self._brightness)
        self._framebuffer[:] = np.asarray(framedata)
        self._matrix.show()
    
    def stop_gif(self):
        """ Sends stop event to show_gif thread and clears the leds """
        if self._gif_thread is None or not self._gif_thread.is_alive():
            return
        if not self._gif_stop_event.is_set():
            self._gif_stop_event.set()
        if self._gif_thread is None:
            return
        else:
            self._gif_thread.join()
            self.clear()
        
    def _show_gif(self, img, stop_event: threading.Event):
        """Extract all frames from gif and show on matrix"""
        imgs = []
        for i in range(img.n_frames):
            img.seek(i)
            frame = Image.new('RGB', img.size)
            frame.paste(img, (0,0))
            frame.thumbnail((self.width, self.height))
            imgs.append((frame.copy(), img.info.get("duration", 100)/1000))
            
        while not stop_event.is_set():
            for frame, duration in imgs:
                self._update_framebuffer(frame)
                time.sleep(duration)
    
    def _show_png(self, img):
        self.stop_gif()
        img.thumbnail((self.width, self.height))
        img = Matrix.remove_alpha(img, color=(0,0,0))
        self._update_framebuffer(img)
    
    def show_img(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError("Image File Does Not Exist")
        img = Image.open(path)
        if img is None:
            return
        if img.format == "GIF":
            self.stop_gif()
            self._gif_stop_event = threading.Event()
            self._gif_thread = threading.Thread(target=self._show_gif, args=(img,self._gif_stop_event))
            self._gif_thread.start()
        else:
            self._show_png(img)
    
    def clear(self):
        self._update_framebuffer(self._blank_img)
        
    def __del__(self):
        self.stop_gif()
        
    @staticmethod
    def remove_alpha(img, color=(255, 255, 255)):
        """Remove the alpha channel from RGBA images"""
        img.load()
        background = Image.new('RGB', img.size, color)
        background.paste(img, mask=img.split()[3])
        return background
        
        