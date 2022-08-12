from checkout import Checkout


def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_calcTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calcTotal() == 1

def test_totalMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calcTotal() == 3

def test_addDiscount(checkout):
    checkout.addDiscount("a", 3, 2)

def test_applyDiscount(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calcTotal() == 2 
