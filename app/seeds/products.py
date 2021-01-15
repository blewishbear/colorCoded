from app.models import db, Product
def seed_products():
    """
    Model:
    Product(title="", category_id=, price=, color_id=, size_id=,  stock=, img_url)

    """
    # for size in range(1,7):
    #     Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=size, color_id= 1, img_url="https://imgur.com/d4lzZ0l")
    #     for color in range(1,6):
            # Product(Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=1, color_id=color, img_url="https://imgur.com/d4lzZ0l"))


    # curl1_xs_red = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=1, color_id= 1, img_url="https://i.imgur.com/d4lzZ0l.png")
    # curl1_sm_red = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=2, color_id= 1, img_url="https://i.imgur.com/d4lzZ0l.png")
    # curl1_m_red = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=3, color_id= 1, img_url="https://i.imgur.com/d4lzZ0l.png")
    curl1_lg_red = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=4, color_id= 1, img_url="https://i.imgur.com/d4lzZ0l.png")
    # curl1_xl_red = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=5, color_id= 1, img_url="https://i.imgur.com/d4lzZ0l.png")
    # curl1_xxl_red = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/d4lzZ0l.png")

    # curl1_xs_blue = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://imgur.com/vcrktFg")
    # curl1_sm_blue = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://imgur.com/vcrktFg")
    # curl1_m_blue = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://imgur.com/vcrktFg")
    curl1_lg_blue = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/vcrktFg.png")
    # curl1_xl_blue = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://imgur.com/vcrktFg")
    # curl1_xxl_blue = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://imgur.com/vcrktFg")

    # curl1_xs_yellow = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/u0qyagf.png")
    # curl1_sm_yellow = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/u0qyagf.png")
    # curl1_m_yellow = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=3, color_id=3,  img_url="https://i.imgur.com/u0qyagf.png")
    curl1_lg_yellow = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/u0qyagf.png")
    # curl1_xl_yellow = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/u0qyagf.png")
    # curl1_xxl_yellow = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/u0qyagf.png")

    # curl1_xs_green = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/e2bJQSI.png")
    # curl1_sm_green = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/e2bJQSI.png")
    # curl1_m_green = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/e2bJQSI.png")
    curl1_lg_green = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/e2bJQSI.png")
    # curl1_xl_green = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/e2bJQSI.png")
    # curl1_xxl_green = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/e2bJQSI.png")

    # curl1_xs_white = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://imgur.com/bHEW5tu")
    # curl1_sm_white = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://imgur.com/bHEW5tu")
    # curl1_m_white = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://imgur.com/bHEW5tu")
    curl1_lg_white = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/bHEW5tu.png")
    # curl1_xl_white = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://imgur.com/bHEW5tu")
    # curl1_xxl_white = Product(title="CurlyBoyKids", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://imgur.com/bHEW5tu")


    # curl2_xs_red = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id= 1, img_url="https://i.imgur.com/omYJgQ1.png")
    # curl2_sm_red = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id= 1, img_url="https://i.imgur.com/omYJgQ1.png")
    # curl2_m_red = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id= 1, img_url="https://i.imgur.com/omYJgQ1.png")
    curl2_lg_red = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id= 1, img_url="https://i.imgur.com/omYJgQ1.png")
    # curl2_xl_red = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id= 1, img_url="https://i.imgur.com/omYJgQ1.png")
    # curl2_xxl_red = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/omYJgQ1.png")

    # curl2_xs_blue = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/S9Y9zW2.png")
    # curl2_sm_blue = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/S9Y9zW2.png")
    # curl2_m_blue = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/S9Y9zW2.png")
    curl2_lg_blue = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/S9Y9zW2.png")
    # curl2_xl_blue = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/S9Y9zW2.png")
    # curl2_xxl_blue = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/S9Y9zW2.png")

    # curl2_xs_yellow = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/JeAMOo3.png")
    # curl2_sm_yellow = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/JeAMOo3.png")
    # curl2_m_yellow = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/JeAMOo3.png")
    curl2_lg_yellow = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/JeAMOo3.png")
    # curl2_xl_yellow = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/JeAMOo3.png")
    # curl2_xxl_yellow = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/JeAMOo3.png")

    # curl2_xs_green = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/RZh5X8B.png")
    # curl2_sm_green = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/RZh5X8B.png")
    # curl2_m_green = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/RZh5X8B.png")
    curl2_lg_green = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/RZh5X8B.png")
    # curl2_xl_green = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/RZh5X8B.png")
    # curl2_xxl_green = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/RZh5X8B.png")

    # curl2_xs_white = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/J8M4AGj.png")
    # curl2_sm_white = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/J8M4AGj.png")
    # curl2_m_white = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/J8M4AGj.png")
    curl2_lg_white = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/J8M4AGj.png")
    # curl2_xl_white = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/J8M4AGj.png")
    # curl2_xxl_white = Product(title="CurlyBoyPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/J8M4AGj.png")


    # curl3_xs_red = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=1, color_id= 1, img_url="https://i.imgur.com/5LdPVkp.png")
    # curl3_sm_red = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=2, color_id= 1, img_url="https://i.imgur.com/5LdPVkp.png")
    # curl3_m_red = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=3, color_id= 1, img_url="https://i.imgur.com/5LdPVkp.png")
    curl3_lg_red = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=4, color_id= 1, img_url="https://i.imgur.com/5LdPVkp.png")
    # curl3_xl_red = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=5, color_id= 1, img_url="https://i.imgur.com/5LdPVkp.png")
    # curl3_xxl_red = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/5LdPVkp.png")

    # curl3_xs_blue = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/z4XFUdn.png")
    # curl3_sm_blue = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/z4XFUdn.png")
    # curl3_m_blue = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/z4XFUdn.png")
    curl3_lg_blue = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/z4XFUdn.png")
    # curl3_xl_blue = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/z4XFUdn.png")
    # curl3_xxl_blue = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/z4XFUdn.png")

    # curl3_xs_yellow = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/zSlRCDK.png")
    # curl3_sm_yellow = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/zSlRCDK.png")
    # curl3_m_yellow = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/zSlRCDK.png")
    curl3_lg_yellow = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/zSlRCDK.png")
    # curl3_xl_yellow = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/zSlRCDK.png")
    # curl3_xxl_yellow = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/zSlRCDK.png")

    # curl3_xs_green = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/o3KmgwM.png")
    # curl3_sm_green = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/o3KmgwM.png")
    # curl3_m_green = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/o3KmgwM.png")
    curl3_lg_green = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/o3KmgwM.png")
    # curl3_xl_green = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/o3KmgwM.png")
    # curl3_xxl_green = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/o3KmgwM.png")

    # curl3_xs_white = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/FbddhVp.png")
    # curl3_sm_white = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/FbddhVp.png")
    # curl3_m_white = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/FbddhVp.png")
    curl3_lg_white = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/FbddhVp.png")
    # curl3_xl_white = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/FbddhVp.png")
    # curl3_xxl_white = Product(title="CurlyBoyTeen", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/FbddhVp.png")


    # curl4_xs_red = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=1, color_id= 1, img_url="https://i.imgur.com/M0uAIO9.png")
    # curl4_sm_red = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=2, color_id= 1, img_url="https://i.imgur.com/M0uAIO9.png")
    # curl4_m_red = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=3, color_id= 1, img_url="https://i.imgur.com/M0uAIO9.png")
    curl4_lg_red = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=4, color_id= 1, img_url="https://i.imgur.com/M0uAIO9.png")
    # curl4_xl_red = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=5, color_id= 1, img_url="https://i.imgur.com/M0uAIO9.png")
    # curl4_xxl_red = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/M0uAIO9.png")

    # curl4_xs_blue = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/cnhD1Pu.png")
    # curl4_sm_blue = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/cnhD1Pu.png")
    # curl4_m_blue = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/cnhD1Pu.png")
    curl4_lg_blue = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/cnhD1Pu.png")
    # curl4_xl_blue = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/cnhD1Pu.png")
    # curl4_xxl_blue = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/cnhD1Pu.png")

    # curl4_xs_yellow = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/Wowo0GF.png")
    # curl4_sm_yellow = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/Wowo0GF.png")
    # curl4_m_yellow = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/Wowo0GF.png")
    curl4_lg_yellow = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/Wowo0GF.png")
    # curl4_xl_yellow = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/Wowo0GF.png")
    # curl4_xxl_yellow = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/Wowo0GF.png")

    # curl4_xs_green = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/X7lpxTL.png")
    # curl4_sm_green = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/X7lpxTL.png")
    # curl4_m_green = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/X7lpxTL.png")
    curl4_lg_green = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/X7lpxTL.png")
    # curl4_xl_green = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/X7lpxTL.png")
    # curl4_xxl_green = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/X7lpxTL.png")

    # curl4_xs_white = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/zt8PPLm.png")
    # curl4_sm_white = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/zt8PPLm.png")
    # curl4_m_white = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/zt8PPLm.png")
    curl4_lg_white = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/zt8PPLm.png")
    # curl4_xl_white = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/zt8PPLm.png")
    # curl4_xxl_white = Product(title="CurlyBoyAdult", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/zt8PPLm.png")


    # cg1_xs_red = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=1, color_id=1, img_url="https://i.imgur.com/3LCDs9j.png")
    # cg1_sm_red = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=2, color_id=1, img_url="https://i.imgur.com/3LCDs9j.png")
    # cg1_m_red = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=3, color_id=1, img_url="https://i.imgur.com/3LCDs9j.png")
    cg1_lg_red = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=4, color_id=1, img_url="https://i.imgur.com/3LCDs9j.png")
    # cg1_xl_red = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=5, color_id=1, img_url="https://i.imgur.com/3LCDs9j.png")
    # cg1_xxl_red = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/3LCDs9j.png")

    # cg1_xs_blue = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/wynwH4S.png")
    # cg1_sm_blue = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/wynwH4S.png")
    # cg1_m_blue = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/wynwH4S.png")
    cg1_lg_blue = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/wynwH4S.png")
    # cg1_xl_blue = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/wynwH4S.png")
    # cg1_xxl_blue = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/wynwH4S.png")

    # cg1_xs_yellow = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/HDRnlTO.png")
    # cg1_sm_yellow = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/HDRnlTO.png")
    # cg1_m_yellow = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/HDRnlTO.png")
    cg1_lg_yellow = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/HDRnlTO.png")
    # cg1_xl_yellow = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/HDRnlTO.png")
    # cg1_xxl_yellow = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/HDRnlTO.png")

    # cg1_xs_green = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/Hv5PVXV.png")
    # cg1_sm_green = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/Hv5PVXV.png")
    # cg1_m_green = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/Hv5PVXV.png")
    cg1_lg_green = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/Hv5PVXV.png")
    # cg1_xl_green = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/Hv5PVXV.png")
    # cg1_xxl_green = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/Hv5PVXV.png")

    # cg1_xs_white = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/Hh6NI9h.png")
    # cg1_sm_white = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/Hh6NI9h.png")
    # cg1_m_white = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/Hh6NI9h.png")
    cg1_lg_white = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/Hh6NI9h.png")
    # cg1_xl_white = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/Hh6NI9h.png")
    # cg1_xxl_white = Product(title="CurlyGirlKid", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/Hh6NI9h.png")


    # cg2_xs_red = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=1, img_url="https://i.imgur.com/3rPPdWl.png")
    # cg2_sm_red = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=1, img_url="https://i.imgur.com/3rPPdWl.png")
    # cg2_m_red = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=1, img_url="https://i.imgur.com/3rPPdWl.png")
    cg2_lg_red = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=1, img_url="https://i.imgur.com/3rPPdWl.png")
    # cg2_xl_red = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=1, img_url="https://i.imgur.com/3rPPdWl.png")
    # cg2_xxl_red = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/3rPPdWl.png")

    # cg2_xs_blue = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/xJiEyms.png")
    # cg2_sm_blue = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/xJiEyms.png")
    # cg2_m_blue = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/xJiEyms.png")
    cg2_lg_blue = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/xJiEyms.png")
    # cg2_xl_blue = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/xJiEyms.png")
    # cg2_xxl_blue = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/xJiEyms.png")

    # cg2_xs_yellow = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/BOSjW7T.png")
    # cg2_sm_yellow = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/BOSjW7T.png")
    # cg2_m_yellow = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/BOSjW7T.png")
    cg2_lg_yellow = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/BOSjW7T.png")
    # cg2_xl_yellow = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/BOSjW7T.png")
    # cg2_xxl_yellow = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/BOSjW7T.png")

    # cg2_xs_green = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/KPMXW8n.png")
    # cg2_sm_green = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/KPMXW8n.png")
    # cg2_m_green = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/KPMXW8n.png")
    cg2_lg_green = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/KPMXW8n.png")
    # cg2_xl_green = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/KPMXW8n.png")
    # cg2_xxl_green = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/KPMXW8n.png")

    # cg2_xs_white = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/D5wZZ5u.png")
    # cg2_sm_white = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/D5wZZ5u.png")
    # cg2_m_white = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/D5wZZ5u.png")
    cg2_lg_white = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/D5wZZ5u.png")
    # cg2_xl_white = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/D5wZZ5u.png")
    # cg2_xxl_white = Product(title="CurlyGirlPreTeen", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/D5wZZ5u.png")


    # cg3_xs_red = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=1, color_id=1, img_url="https://i.imgur.com/xI208h4.png")
    # cg3_sm_red = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=2, color_id=1, img_url="https://i.imgur.com/xI208h4.png")
    # cg3_m_red = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=3, color_id=1, img_url="https://i.imgur.com/xI208h4.png")
    cg3_lg_red = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=4, color_id=1, img_url="https://i.imgur.com/xI208h4.png")
    # cg3_xl_red = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=5, color_id=1, img_url="https://i.imgur.com/xI208h4.png")
    # cg3_xxl_red = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/xI208h4.png")

    # cg3_xs_blue = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/4HdvrkF.png")
    # cg3_sm_blue = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/4HdvrkF.png")
    # cg3_m_blue = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/4HdvrkF.png")
    cg3_lg_blue = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/4HdvrkF.png")
    # cg3_xl_blue = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/4HdvrkF.png")
    # cg3_xxl_blue = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/4HdvrkF.png")

    # cg3_xs_yellow = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/sYa2xp8.png")
    # cg3_sm_yellow = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/sYa2xp8.png")
    # cg3_m_yellow = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/sYa2xp8.png")
    cg3_lg_yellow = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/sYa2xp8.png")
    # cg3_xl_yellow = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/sYa2xp8.png")
    # cg3_xxl_yellow = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/sYa2xp8.png")

    # cg3_xs_green = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/KGqMIp6.png")
    # cg3_sm_green = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/KGqMIp6.png")
    # cg3_m_green = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/KGqMIp6.png")
    cg3_lg_green = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/KGqMIp6.png")
    # cg3_xl_green = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/KGqMIp6.png")
    # cg3_xxl_green = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/KGqMIp6.png")

    # cg3_xs_white = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/pgNQBAS.png")
    # cg3_sm_white = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/pgNQBAS.png")
    # cg3_m_white = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/pgNQBAS.png")
    cg3_lg_white = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/pgNQBAS.png")
    # cg3_xl_white = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/pgNQBAS.png")
    # cg3_xxl_white = Product(title="CurlyGirlTeen", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/pgNQBAS.png")


    # cg4_xs_red = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=1, color_id=1, img_url="https://i.imgur.com/7ai1pft.png")
    # cg4_sm_red = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=2, color_id=1, img_url="https://i.imgur.com/7ai1pft.png")
    # cg4_m_red = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=3, color_id=1, img_url="https://i.imgur.com/7ai1pft.png")
    cg4_lg_red = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=4, color_id=1, img_url="https://i.imgur.com/7ai1pft.png")
    # cg4_xl_red = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=5, color_id=1, img_url="https://i.imgur.com/7ai1pft.png")
    # cg4_xxl_red = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=6, color_id=1, img_url="https://i.imgur.com/7ai1pft.png")

    # cg4_xs_blue = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=1, color_id=2, img_url="https://i.imgur.com/FHmb1of.png")
    # cg4_sm_blue = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=2, color_id=2, img_url="https://i.imgur.com/FHmb1of.png")
    # cg4_m_blue = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=3, color_id=2, img_url="https://i.imgur.com/FHmb1of.png")
    cg4_lg_blue = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=4, color_id=2, img_url="https://i.imgur.com/FHmb1of.png")
    # cg4_xl_blue = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=5, color_id=2, img_url="https://i.imgur.com/FHmb1of.png")
    # cg4_xxl_blue = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=6, color_id=2, img_url="https://i.imgur.com/FHmb1of.png")

    # cg4_xs_yellow = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=1, color_id=3, img_url="https://i.imgur.com/igdeQQD.png")
    # cg4_sm_yellow = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=2, color_id=3, img_url="https://i.imgur.com/igdeQQD.png")
    # cg4_m_yellow = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=3, color_id=3, img_url="https://i.imgur.com/igdeQQD.png")
    cg4_lg_yellow = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=4, color_id=3, img_url="https://i.imgur.com/igdeQQD.png")
    # cg4_xl_yellow = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=5, color_id=3, img_url="https://i.imgur.com/igdeQQD.png")
    # cg4_xxl_yellow = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=6, color_id=3, img_url="https://i.imgur.com/igdeQQD.png")

    # cg4_xs_green = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=1, color_id=4, img_url="https://i.imgur.com/e3iPYvG.png")
    # cg4_sm_green = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=2, color_id=4, img_url="https://i.imgur.com/e3iPYvG.png")
    # cg4_m_green = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=3, color_id=4, img_url="https://i.imgur.com/e3iPYvG.png")
    cg4_lg_green = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=4, color_id=4, img_url="https://i.imgur.com/e3iPYvG.png")
    # cg4_xl_green = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=5, color_id=4, img_url="https://i.imgur.com/e3iPYvG.png")
    # cg4_xxl_green = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=6, color_id=4, img_url="https://i.imgur.com/e3iPYvG.png")

    # cg4_xs_white = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=1, color_id=5, img_url="https://i.imgur.com/xVevx8c.png")
    # cg4_sm_white = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=2, color_id=5, img_url="https://i.imgur.com/xVevx8c.png")
    # cg4_m_white = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=3, color_id=5, img_url="https://i.imgur.com/xVevx8c.png")
    cg4_lg_white = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=4, color_id=5, img_url="https://i.imgur.com/xVevx8c.png")
    # cg4_xl_white = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=5, color_id=5, img_url="https://i.imgur.com/xVevx8c.png")
    # cg4_xxl_white = Product(title="CurlyGirlAdult", category_id=1, price=20, stock=30, size_id=6, color_id=5, img_url="https://i.imgur.com/xVevx8c.png")

    react_native_xs_red = Product(title="ReactNative", category_id=1, price=20, color_id=1, size_id=1,  stock=30, img_url="https://i.imgur.com/g5KZ475.png")
    react_native_sm_black = Product(title="ReactNative", category_id=1, price=20, color_id=6, size_id=2,  stock=30, img_url="https://i.imgur.com/oxTOQen.png")
    react_native_m_yellow = Product(title="ReactNative", category_id=1, price=20, color_id=3, size_id=3,  stock=30, img_url="https://i.imgur.com/bzqv8m5.png")
    react_native_lg_green = Product(title="ReactNative", category_id=1, price=20, color_id=4, size_id=4,  stock=30, img_url="https://i.imgur.com/5IJPyPa.png")
    react_native_xl_white = Product(title="ReactNative", category_id=1, price=20, color_id=5, size_id=5,  stock=30, img_url="https://i.imgur.com/qYgawqc.png")








    # products = [ curl1_xs_red, curl1_sm_red, curl1_m_red, curl1_lg_red, curl1_xl_red, curl1_xxl_red,
    #              curl1_xs_blue, curl1_sm_blue, curl1_m_blue, curl1_lg_blue, curl1_xl_blue, curl1_xxl_blue,
    #              curl1_xs_yellow, curl1_sm_yellow, curl1_m_yellow, curl1_lg_yellow, curl1_xl_yellow, curl1_xxl_yellow,
    #              curl1_xs_green, curl1_sm_green, curl1_m_green, curl1_lg_green, curl1_xl_green, curl1_xxl_green,
    #              curl1_xs_white, curl1_sm_white, curl1_m_white, curl1_lg_white, curl1_xl_white, curl1_xxl_white,

    #              curl2_xs_red, curl2_sm_red, curl2_m_red, curl2_lg_red, curl2_xl_red, curl2_xxl_red,
    #              curl2_xs_blue, curl2_sm_blue, curl2_m_blue, curl2_lg_blue, curl2_xl_blue, curl2_xxl_blue,
    #              curl2_xs_yellow, curl2_sm_yellow, curl2_m_yellow, curl2_lg_yellow, curl2_xl_yellow, curl2_xxl_yellow,
    #              curl2_xs_green, curl2_sm_green, curl2_m_green, curl2_lg_green, curl2_xl_green, curl2_xxl_green,
    #              curl2_xs_white, curl2_sm_white, curl2_m_white, curl2_lg_white, curl2_xl_white, curl2_xxl_white,

    #              curl3_xs_red, curl3_sm_red, curl3_m_red, curl3_lg_red, curl3_xl_red, curl3_xxl_red,
    #              curl3_xs_blue, curl3_sm_blue, curl3_m_blue, curl3_lg_blue, curl3_xl_blue, curl3_xxl_blue,
    #              curl3_xs_yellow, curl3_sm_yellow, curl3_m_yellow, curl3_lg_yellow, curl3_xl_yellow, curl3_xxl_yellow,
    #              curl3_xs_green, curl3_sm_green, curl3_m_green, curl3_lg_green, curl3_xl_green, curl3_xxl_green,
    #              curl3_xs_white, curl3_sm_white, curl3_m_white, curl3_lg_white, curl3_xl_white, curl3_xxl_white,

    #              cg1_xs_red, cg1_sm_red, cg1_m_red, cg1_lg_red, cg1_xl_red, cg1_xxl_red,
    #              cg1_xs_blue, cg1_sm_blue, cg1_m_blue, cg1_lg_blue, cg1_xl_blue, cg1_xxl_blue,
    #              cg1_xs_yellow, cg1_sm_yellow, cg1_m_yellow, cg1_lg_yellow, cg1_xl_yellow, cg1_xxl_yellow,
    #              cg1_xs_green, cg1_sm_green, cg1_m_green, cg1_lg_green, cg1_xl_green, cg1_xxl_green,
    #              cg1_xs_white, cg1_sm_white, cg1_m_white, cg1_lg_white, cg1_xl_white, cg1_xxl_white,
    #              cg1_xs_red, cg1_sm_red, cg1_m_red, cg1_lg_red, cg1_xl_red, cg1_xxl_red,

    #              cg2_xs_red, cg2_sm_red, cg2_m_red, cg2_lg_red, cg2_xl_red, cg2_xxl_red,
    #              cg2_xs_blue, cg2_sm_blue, cg2_m_blue, cg2_lg_blue, cg2_xl_blue, cg2_xxl_blue,
    #              cg2_xs_yellow, cg2_sm_yellow, cg2_m_yellow, cg2_lg_yellow, cg2_xl_yellow, cg2_xxl_yellow,
    #              cg2_xs_green, cg2_sm_green, cg2_m_green, cg2_lg_green, cg2_xl_green, cg2_xxl_green,
    #              cg2_xs_white, cg2_sm_white, cg2_m_white, cg2_lg_white, cg2_xl_white, cg2_xxl_white,
    #              cg2_xs_red, cg2_sm_red, cg2_m_red, cg2_lg_red, cg2_xl_red, cg2_xxl_red,

    #              cg3_xs_red, cg3_sm_red, cg3_m_red, cg3_lg_red, cg3_xl_red, cg3_xxl_red,
    #              cg3_xs_blue, cg3_sm_blue, cg3_m_blue, cg3_lg_blue, cg3_xl_blue, cg3_xxl_blue,
    #              cg3_xs_yellow, cg3_sm_yellow, cg3_m_yellow, cg3_lg_yellow, cg3_xl_yellow, cg3_xxl_yellow,
    #              cg3_xs_green, cg3_sm_green, cg3_m_green, cg3_lg_green, cg3_xl_green, cg3_xxl_green,
    #              cg3_xs_white, cg3_sm_white, cg3_m_white, cg3_lg_white, cg3_xl_white, cg3_xxl_white,
    #              cg3_xs_red, cg3_sm_red, cg3_m_red, cg3_lg_red, cg3_xl_red, cg3_xxl_red,

    #              cg4_xs_red, cg4_sm_red, cg4_m_red, cg4_lg_red, cg4_xl_red, cg4_xxl_red,
    #              cg4_xs_blue, cg4_sm_blue, cg4_m_blue, cg4_lg_blue, cg4_xl_blue, cg4_xxl_blue,
    #              cg4_xs_yellow, cg4_sm_yellow, cg4_m_yellow, cg4_lg_yellow, cg4_xl_yellow, cg4_xxl_yellow,
    #              cg4_xs_green, cg4_sm_green, cg4_m_green, cg4_lg_green, cg4_xl_green, cg4_xxl_green,
    #              cg4_xs_white, cg4_sm_white, cg4_m_white, cg4_lg_white, cg4_xl_white, cg4_xxl_white,
    #              cg4_xs_red, cg4_sm_red, cg4_m_red, cg4_lg_red, cg4_xl_red, cg4_xxl_red,
                #  ]
    products = [
    curl1_lg_red, curl1_lg_blue, curl1_lg_yellow, curl1_lg_green, curl1_lg_white,
    curl2_lg_red, curl2_lg_blue, curl2_lg_yellow, curl2_lg_green, curl2_lg_white,
    curl3_lg_red, curl3_lg_blue, curl3_lg_yellow, curl3_lg_green, curl3_lg_white,
    curl4_lg_red, curl4_lg_blue, curl4_lg_yellow, curl4_lg_green, curl4_lg_white,
    cg1_lg_red, cg1_lg_blue, cg1_lg_yellow, cg1_lg_green, cg1_lg_white,
    cg2_lg_red, cg2_lg_blue, cg2_lg_yellow, cg2_lg_green, cg2_lg_white,
    cg3_lg_red, cg3_lg_blue, cg3_lg_yellow, cg3_lg_green, cg3_lg_white,
    cg4_lg_red, cg4_lg_blue, cg4_lg_yellow, cg4_lg_green, cg4_lg_white,
    react_native_xs_red, react_native_sm_black, react_native_m_yellow, react_native_lg_green, react_native_xl_white
    ]
    for product in products:
        db.session.add(product)

    db.session.commit()

def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
