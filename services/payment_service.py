def promote_listing(user,ticket):

    if user.wallet>=20:

        user.wallet-=20

        ticket.featured=True

        return True

    return False
