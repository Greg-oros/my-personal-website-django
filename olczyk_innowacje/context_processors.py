# myapp/context_processors.py
import random
import math


def shooting_stars(request):
    stars = []
    for _ in range(20):
        top = random.uniform(0, 80)
        left = random.uniform(0, 80)
        delay = random.uniform(0, 3)
        dx = random.uniform(-800, 800)
        dy = random.uniform(-800, 800)
        angle = math.degrees(math.atan2(dy, dx))
        stars.append(
            {
                "top": top,
                "left": left,
                "delay": delay,
                "dx": dx,
                "dy": dy,
            }
        )
    return {"stars": stars}
