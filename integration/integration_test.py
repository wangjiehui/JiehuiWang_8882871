import stringUtil
def test_integration1():
    assert stringUtil.removeString(stringUtil.addString("abcabc", "dddd"), "d") == "abcabc"
def test_integration2():
    assert stringUtil.removeString(stringUtil.addString("abcabc", "dddd"), "d") == "abc"


# Unit testing

def test_addStr():
    assert stringUtil.addString("a", "b") == "ab"

def test_removeStr():
    assert stringUtil.removeString("abcddddd", "d") == "abc"

