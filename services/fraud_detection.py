from models.ticket import Ticket

def check_duplicate_pnr(pnr):

    ticket=Ticket.query.filter_by(pnr=pnr).first()

    return ticket is not None


def suspicious_price(price):

    if price<50:

        return True

    return False
