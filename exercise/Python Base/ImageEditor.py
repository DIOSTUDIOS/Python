import cv2
import numpy as np
from PIL import Image


class PhotoEditor:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert('RGB')
        self.array = np.array(self.image).astype(np.float32) / 255.0

    # 基础调整方法
    def adjust_exposure(self, value):
        """调整曝光度 (-1到1)"""
        self.array = np.clip(self.array * (1 + value), 0, 1)

    def adjust_contrast(self, value):
        """调整对比度 (建议0-2)"""
        mean = np.mean(self.array)
        self.array = np.clip((self.array - mean) * value + mean, 0, 1)

    def adjust_brightness(self, value):
        """调整亮度 (-1到1)"""
        self.array = np.clip(self.array + value, 0, 1)

    # 颜色调整方法
    def adjust_saturation(self, value):
        """调整饱和度 (-1到1)"""
        hsv = self._rgb_to_hsv()
        hsv[..., 1] = np.clip(hsv[..., 1] * (1 + value), 0, 1)
        self.array = self._hsv_to_rgb(hsv)

    def adjust_vibrance(self, value):
        """自然饱和度 (-1到1)"""
        hsv = self._rgb_to_hsv()
        s = hsv[..., 1]
        adjust = value * (1 - s)  # 对低饱和区域增强更多
        hsv[..., 1] = np.clip(s + adjust, 0, 1)
        self.array = self._hsv_to_rgb(hsv)

    def adjust_temperature(self, value):
        """色温调整 (-1冷色到1暖色)"""
        self.array[..., 0] *= (1 + value)  # 红色通道
        self.array[..., 2] *= (1 - value)  # 蓝色通道
        self.array = np.clip(self.array, 0, 1)

    def adjust_tint(self, value):
        """色调调整 (-1绿到1品红)"""
        self.array[..., 1] *= (1 + value)  # 绿色通道
        self.array = np.clip(self.array, 0, 1)

    # 高级调整方法
    def adjust_highlights(self, value):
        """高光调整 (-1到1)"""
        hsv = self._rgb_to_hsv()
        mask = hsv[..., 2] > 0.7
        hsv[..., 2][mask] = np.clip(hsv[..., 2][mask] + value, 0, 1)
        self.array = self._hsv_to_rgb(hsv)

    def adjust_shadows(self, value):
        """阴影调整 (-1到1)"""
        hsv = self._rgb_to_hsv()
        mask = hsv[..., 2] < 0.3
        hsv[..., 2][mask] = np.clip(hsv[..., 2][mask] + value, 0, 1)
        self.array = self._hsv_to_rgb(hsv)

    def adjust_sharpness(self, value):
        """锐度调整 (0-1)"""
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]]) * value
        sharpened = cv2.filter2D(self.array, -1, kernel)
        self.array = np.clip(sharpened, 0, 1)

    def adjust_vignette(self, strength):
        """晕影效果 (0-1)"""
        rows, cols = self.array.shape[:2]
        x = np.linspace(-1, 1, cols)
        y = np.linspace(-1, 1, rows)
        X, Y = np.meshgrid(x, y)
        mask = 1 - np.sqrt(X ** 2 + Y ** 2) * strength
        mask = np.clip(mask, 0, 1)[..., np.newaxis]
        self.array = np.clip(self.array * mask, 0, 1)

    # 工具方法
    def _rgb_to_hsv(self):
        """RGB转HSV颜色空间"""
        return cv2.cvtColor(self.array, cv2.COLOR_RGB2HSV)

    def _hsv_to_rgb(self, hsv):
        """HSV转RGB颜色空间"""
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    def save(self, output_path):
        """保存处理后的图片"""
        output_array = (self.array * 255).astype(np.uint8)
        Image.fromarray(output_array).save(output_path)


# 使用示例
if __name__ == "__main__":
    editor = PhotoEditor("input.jpg")

    # 应用各种调整
    editor.adjust_exposure(0.2)  # 增加曝光
    editor.adjust_brightness(0.8)
    editor.adjust_contrast(1.1)  # 提高对比度
    editor.adjust_saturation(0.3)  # 增加饱和度
    editor.adjust_temperature(-0.1)  # 稍微冷色调
    editor.adjust_sharpness(0.2)  # 增加锐度
    editor.adjust_vignette(0.3)  # 添加晕影效果

    editor.save("output.jpg")
