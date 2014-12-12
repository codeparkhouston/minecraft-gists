import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
    x, y, z = mc.player.getPos()
    block = 38
    mc.setBlock(x, y, z, block)
    time.sleep(0.2)