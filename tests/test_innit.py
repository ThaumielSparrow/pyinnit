import pythinnit


def test_innit_is_constructor():
    class Wanker:
        def __innit__(self, bloke):
            self.bloke = bloke

    wanker = Wanker("oi") # type: ignore[call-arg]

    assert wanker.bloke == "oi"
    assert Wanker.__init__ is Wanker.__innit__


def test_normal_init_still_works():
    class Tea:
        def __init__(self, milk):
            self.milk = milk

    tea = Tea(True)

    assert tea.milk is True
    assert Tea.__innit__ is Tea.__init__


def test_init_wins_if_both_are_defined():
    class Argument:
        def __init__(self):
            self.result = "init"

        def __innit__(self):
            self.result = "innit"

    obj = Argument()

    assert obj.result == "init"