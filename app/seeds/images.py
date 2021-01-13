def seed_images():
    """
    Model:
    Image(product_id=, color_id="", img_url="")

    """


    cb1_red_kid = Image(product_id=1, color_id=1, img_url="https://imgur.com/d4lzZ0l")
    cb1_red_kid = Image(product_id=2, color_id=1, img_url="https://imgur.com/d4lzZ0l")
    cb1_red_kid = Image(product_id=3, color_id=1, img_url="https://imgur.com/d4lzZ0l")
    cb1_red_kid = Image(product_id=4, color_id=1, img_url="https://imgur.com/d4lzZ0l")
    cb1_red_kid = Image(product_id=5, color_id=1, img_url="https://imgur.com/d4lzZ0l")
    cb1_red_kid = Image(product_id=6, color_id=1, img_url="https://imgur.com/d4lzZ0l")

    cb1_blue_kid = Image(product_id=7, color_id=1, img_url="https://imgur.com/vcrktFg")
    cb1_blue_kid = Image(product_id=8, color_id=1, img_url="https://imgur.com/vcrktFg")
    cb1_blue_kid = Image(product_id=9, color_id=1, img_url="https://imgur.com/vcrktFg")
    cb1_blue_kid = Image(product_id=10, color_id=1, img_url="https://imgur.com/vcrktFg")
    cb1_blue_kid = Image(product_id=11, color_id=1, img_url="https://imgur.com/vcrktFg")
    cb1_blue_kid = Image(product_id=12, color_id=1, img_url="https://imgur.com/vcrktFg")

    # cb1_yellow_kid = Image(product_id=13, color_id=1, img_url="https://imgur.com/u0qyagf")
    # cb1_yellow_kid = Image(product_id=14, color_id=1, img_url="https://imgur.com/u0qyagf")
    # cb1_yellow_kid = Image(product_id=15, color_id=1, img_url="https://imgur.com/u0qyagf")
    # cb1_yellow_kid = Image(product_id=16, color_id=1, img_url="https://imgur.com/u0qyagf")
    # cb1_yellow_kid = Image(product_id=17, color_id=1, img_url="https://imgur.com/u0qyagf")
    # cb1_yellow_kid = Image(product_id=18, color_id=1, img_url="https://imgur.com/u0qyagf")

    # cb1_green_kid = Image(product_id=17, color_id=1, img_url="https://imgur.com/e2bJQSI")
    # cb1_green_kid = Image(product_id=18, color_id=1, img_url="https://imgur.com/e2bJQSI")
    # cb1_green_kid = Image(product_id=19, color_id=1, img_url="https://imgur.com/e2bJQSI")
    # cb1_green_kid = Image(product_id=20, color_id=1, img_url="https://imgur.com/e2bJQSI")
    # cb1_green_kid = Image(product_id=21, color_id=1, img_url="https://imgur.com/e2bJQSI")
    # cb1_green_kid = Image(product_id=22, color_id=1, img_url="https://imgur.com/e2bJQSI")







    images = [ idea1, idea2, idea3, idea4, idea5, idea6, idea7 ]
    for image in images:
        db.session.add(image)

    db.session.commit()

def undo_images():
    db.session.execute('TRUNCATE images RESTART IDENTITY CASCADE;')
    db.session.commit()
