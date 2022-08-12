from tabnanny import check
from checkout import Checkout


def checkout():
    checkout = Checkout()
    return checkout

def test_calcTotal(checkout):
    checkout.addItemProce("a",1)
    checkout.addItem("a")
    assert checkout.calcTotal() == 1