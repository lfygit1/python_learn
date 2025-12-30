import pytest
@pytest.fixture(scope="function") # 设置fixture的作用域为方法级别
def init_function():
    print("开始执行方法级别的前置")
    yield
    print("开始执行方法级别的后置")
@pytest.fixture(scope="function")
def init_function02():
    print("开始执行方法级别的前置02")
    yield
    print("开始执行方法级别的后置02")

@pytest.fixture(scope="function")
def init_function03():
    print("开始执行方法级别的前置03")
    num = 1+1
    yield num
    print("开始执行方法级别的后置03")