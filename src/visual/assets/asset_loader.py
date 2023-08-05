from pygame import image


asset_icons = {
    "energy": image.load("src/visual/assets/icon/energy.png"),
    "furnace": image.load("src/visual/assets/icon/furnace.png"),
    "health": image.load("src/visual/assets/icon/health.png"),
    "mining": image.load("src/visual/assets/icon/mining.png"),
    "shield": image.load("src/visual/assets/icon/shield.png"),
    "sword": image.load("src/visual/assets/icon/sword.png")
}

asset_keystone = {
    "frame": image.load("src/visual/assets/passive/keystone/frame.png"),
    "inner": image.load("src/visual/assets/passive/keystone/inner.png")
}

asset_notable = {
    "frame": image.load("src/visual/assets/passive/notable/frame.png"),
    "inner": image.load("src/visual/assets/passive/notable/inner.png")
}

asset_small = {
    "frame": image.load("src/visual/assets/passive/small/frame.png"),
    "inner": image.load("src/visual/assets/passive/small/inner.png")
}