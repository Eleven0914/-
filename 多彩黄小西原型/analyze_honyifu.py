from PIL import Image
from collections import Counter
import colorsys

def get_palette(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        # Resize for faster processing
        img = img.resize((150, 150))
        pixels = list(img.getdata())
        
        # Count colors
        color_counts = Counter(pixels)
        
        # Group by similarity to find dominant visual colors
        # We specifically want a RED and a GREY/SILVER
        
        reds = []
        greys = []
        
        for color, count in color_counts.most_common(5000):
            r, g, b = color
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            h_deg = h * 360
            
            # Check for Red (Hue 0-10 or 345-360, Saturation > 0.4, Value > 0.4)
            if (h_deg <= 15 or h_deg >= 340) and s > 0.4 and v > 0.3:
                reds.append((count, color))
                
            # Check for Grey/Silver (Saturation < 0.15, Value > 0.4 and < 0.9)
            if s < 0.15 and v > 0.3 and v < 0.95:
                greys.append((count, color))
                
        # Get most common red and grey
        dominant_red = sorted(reds, key=lambda x: x[0], reverse=True)[0][1] if reds else (255, 0, 0)
        dominant_grey = sorted(greys, key=lambda x: x[0], reverse=True)[0][1] if greys else (128, 128, 128)
        
        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

        print(f"Red: {rgb_to_hex(dominant_red)}")
        print(f"Grey: {rgb_to_hex(dominant_grey)}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_palette("/Users/fengliuyi/Desktop/MD文件/多彩黄小西原型/honyifu.png")
