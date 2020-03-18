#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------------------------------------------------------

@Author: Bamboo
@Email: bamboo8493@126.com
@Datetime: 2019/10/9 9:58
@Description: class

类成员：
    # 字段
        - 普通字段，保存在对象中，执行只能通过对象访问
        - 静态字段，保存在类中，  执行 可以通过对象访问 也可以通过类访问

    # 方法
        - 普通方法，保存在类中，由对象来调用，self=》对象
        - 静态方法，保存在类中，由类直接调用
        -   类方法，保存在类中，由类直接调用，cls=》当前类

    # 应用场景：
        如果对象中需要保存一些值，执行某功能时，需要使用对象中的值　－＞　普通方法
        不需要任何对象中的值，静态方法

------------------------------------------------------------------------------------------------------------------------

@Modifier: 
@Email: 
@Datetime: 2019/10/9 9:58
@Description: 

------------------------------------------------------------------------------------------------------------------------
"""

"""
# version 1 => define
class Bar:
    def foo(self, arg): print(arg)

bar = Bar()
bar.foo('bar')
bar2 = Bar()
bar2.foo('bar2')
"""

"""
# version 2 => self
class Bar:
    def foo(self, action): print(self.name, self.age, self.gender, action)

bar = Bar()
bar.name = 'bar'
bar.age = 18
bar.gender = 'male'
bar.foo('去山上砍柴')
bar.foo('去山上放羊')
bar.foo('去山上看马撒尿')
"""

"""
# version 3 => constructor => __init__ => 封装
class Bar:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def foo(self, action): print(self.name, self.age, self.gender, action)

bar = Bar('bar', 18, 'male')
bar.foo('去山上砍柴')
bar.foo('去山上放羊')
bar.foo('去山上看马撒尿')
"""

"""
# version 4 => 继承 => all


class Father:
    def bar(self): print('bar')


class Child(Father):
    def foo(self): print('foo')

child = Child()
child.foo()
child.bar()
"""

"""
# version 4 => 继承 => override


class Father:
    def bar(self): print('father bar')


class Child(Father):
    def foo(self): print('foo')
    def bar(self):
        # 执行父类(基类)方法
        super(Child, self).bar()
        # Father.bar(self)
        print('child bar')

child = Child()
child.foo()
child.bar()
"""

"""
# version 5 => 继承多个父类
# 注意：当继承多个父类时，并且父类中都有同名成员时，优先使用左侧的父类（也就是第一个父类）


class Father:
    def bar(self): print('father bar')

class Father2:
    def bar2(self): print('father2 bar')


class Child(Father, Father2):
    def bar(self): print('child bar')

child = Child()
child.bar()
child.bar2()
"""

"""
# version 6 => 继承多个父类，父类又有继承的父类（爷爷类）
# 注意：当继承多个父类时，优先往左侧父类的继承类链查找，若都找不到，再往右侧父类找。。。


class GrandFather:
    def bar2(self): print('grandFather bar')

class Father(GrandFather):
    def bar(self): print('father bar')

class Father2:
    def bar2(self): print('father2 bar')


class Child(Father, Father2):
    def bar(self): print('child bar')

child = Child()
child.bar()
child.bar2()
"""

"""
# version 7 => 继承多个父类，父类有共同的父类（爷爷类）
# 注意：当继承多个父类时，优先往左侧父类(继承类链)查找，若找不到，再往右侧父类找，若找不到，再往公共父类找。。。


class GrandFather:
    def bar2(self): print('grandFather bar')


class Father(GrandFather):
    def bar(self): print('father bar')


class Father2(GrandFather):
    def bar2(self): print('father2 bar')


class Child(Father, Father2):
    def bar(self): print('child bar')


child = Child()
child.bar2()
"""

"""
# version 8 => 继承多个父类，调用右侧父类的方法，
# 在该方法内再调用实例左侧父类和该方法类都有的方法，此时真正调用的是实例左侧父类的方法


class GrandFather:
    def foo(self): print('grandFather foo')


class Father():
    def bar(self): print('father bar')
    def foo(self): print('father foo')


class Father2(GrandFather):
    def bar2(self):
        print('father2 bar')
        self.foo()
    def foo(self): print('father2 foo')


class Child(Father, Father2):
    def bar(self): print('child bar')


child = Child()
child.bar2()
"""

"""
# version 9 => 继承多个父类，实例化子类时，会默认调用子类的 __init__ 方法，
# 若子类未定义，则会调用父类的 __init__ 方法，
# 若再想调用爷爷类的 __init__ 方法，可在父类的 __init__ 方法内调用爷爷类的 __init__ 方法


class GrandFather:
    def __init__(self): print('grandFather __init__')


class Father(GrandFather):
    def __init__(self):
        print('Father2 __init__')
        GrandFather.__init__(self)

z
class Child(Father):
    pass


child = Child()
"""

"""
# version 10 => 静态字段

class Province:
    # 类和实例共有静态字段
    country = '中国'

    def __init__(self, name):
        # 实例私有字段
        self.name = name

province = Province('广东')
print(province.name)
print(province.country)
print(Province.country)
"""

"""
# version 11 => 静态方法

class Foo:
    # 普通方法
    def bar(self): print('bar')

    # 静态方法
    @staticmethod
    def static_method(): print('static_method self is no necessary')

    # 静态方法: 带参数
    @staticmethod
    def static_method_arg(name): print('static_method also can receive arguments %s' % name)

foo = Foo()
foo.static_method()
Foo.static_method_arg('go')
"""

"""
# version 12 => 类方法


class Foo:
    # 类方法: 至少带一个参数
    # param: cls => 当前类
    @classmethod
    def class_method(cls): print('static_method also can receive arguments %s' % cls)


Foo.class_method()
"""

"""
# version 12 => 类属性 => 写法一


class Foo:
    # 类属性(getter): 定义形式是方法，调用形式是属性
    @property
    def perr(self):
        print('getter' , self)
        return 1

    @perr.setter
    def perr(self, val): print('setter', val)

    @perr.deleter
    def perr(self): print('delete')

foo = Foo()

print(foo.perr)

foo.perr = 123

del foo.perr
"""

"""
# version 13 => 类属性 => 写法二


class Foo:
    def method_fget(self): print('get', 123)

    def method_fset(self, val): print('set', val)

    def method_fdel(self): print('delete')

    # 全写
    # per = property(fget=method_fget, fset=method_fset, fdel=method_fdel, doc='@property simple written')
    # 简写
    per = property(method_fget, method_fset, method_fdel, '@property simple written')

    # fget ==
    # @property
    # def per(self): print('get', 123)


foo = Foo()

foo.per

foo.per = 456

del foo.per
"""

"""
# version 14 => 类属性应用 => 分页器


class Pagination:
    def __init__(self, page, page_size=10):
        try:
            current_page = int(page)
        except Exception as e:
            current_page = 1

        self.page = current_page
        self.page_size = page_size

    @property
    def start(self):
        return (self.page - 1) * self.page_size

    @property
    def end(self):
        return self.page * self.page_size


list = []

for i in range(1000): list.append(i)

while True:
    page = input('Please input page number >>: ')
    pagination = Pagination(page)
    print(list[pagination.start:pagination.end])
"""

"""
# version 15 => 成员修饰符 => 公有（默认）、私有
class Foo:
    # 私有静态字段
    __money = 'infinity'

    def __init__(self, name, age):
        # 公有
        self.name = name
        # 私有
        self.__age = age

    def get_age(self): return self.__age

    @staticmethod
    def get_money(): return Foo.__money

    # 私有方法
    def __method(self): return 18

    def call_method(self): return self.__method()

foo = Foo('bamboo', 18)
print(foo.name)
# print(foo.__age)
print(foo.get_age())
# print(Foo.__money)
print(foo.get_money())
print(foo.call_method())
"""

"""
# version 16 => 子类无法访问父类私有成员
class Father:
    def __init__(self):
        self.__age = 18

class Child(Father):
    def __init__(self, name):
        self.name = name
        super(Child, self).__init__()

    def get_age(self): return self.__age

child = Child('bamboo')
print(child.get_age())
"""

"""
# version 17 => 特殊成员
class Foo:
    def __init__(self, name, age):
        print('init')
        self.name = name
        self.age = age

    # 实例() / 对象() 自动执行该函数
    def __call__(self, *args, **kwargs): print('call')

    # int 类实例方法
    def __int__(self):
        print('int')
        return 123

    # str 类实例方法 => 常用于打印 实例成员 / 对象属性
    def __str__(self):
        # print('str')
        # return 'str'
        return '%s-%d' % (self.name, self.age)

    # add 类实例方法 => 两个对象相加时，自动执行第一个对象的 __add__ 方法，并且将第二个对象当作参数传递进入
    def __add__(self, other):
        return self.age + other.age

    # del 关键字，对象被销毁时，自动执行
    def __del__(self):
        print('析构方法')

    # li[8] 获取对象索引时执行
    def __getitem__(self, item):
        # return item + 10
        print(item, type(item))

        if type(item) is slice:
            print('调用者希望内部做切片处理')
            print(item.start, item.stop, item.step)
        else:
            print('调用者希望内部做索引处理')

    # li[8] 设置对象索引时执行
    def __setitem__(self, key, value): print(key, value)

    # li[8] 删除对象索引时执行
    def __delitem__(self, key): print(key)

    # 如果类中有 __iter__ 方法，对象 => 可迭代对象，对象.__iter__() 的返回值 => 迭代器
    def __iter__(self):
        return iter([11, 22, 33])

foo = Foo('bamboo', 18)
# foo()
# print(int(foo))
# print(str(foo))
# print(str(foo))
# print(foo)

# foo2 = Foo('eric', 99)
#
# print(foo + foo2)
#
# print(foo.__dict__)
#
# print(Foo.__dict__)
#
# print(foo[12])
#
# foo[123] = 'ags'
#
# del foo[11]

# foo[12]
# foo[1:4:2]

for item in foo: print(item)
"""

"""
# version 18 => 特殊成员: metaclass
"""


# when the data create, default to call type
class MyType(type):
    # when then class Foo define, the metaclass __init__ will called
    def __init__(self, *args, **kwargs): print('MyType init')

    # self point Foo
    def __call__(self, *args, **kwargs):
        print('MyType call')
        obj = self.__new__(self, *args, **kwargs)
        return self.__init__(obj)


# class extend type object, use metaclass to change class extend chain
class Foo(object, metaclass=MyType):
    def __init__(self):
        print('foo init')
        return self

    def __new__(cls, *args, **kwargs):
        print('foo new')
        return object.__new__(cls, *args, **kwargs)


print(Foo())
