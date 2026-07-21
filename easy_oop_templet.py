from abc import ABC, abstractmethod


# =========================
# 1. 抽象基类 Student
# =========================

class Student(ABC):
    """
    所有学生共同拥有：
    1. 姓名
    2. 年龄

    但是不同类型学生的成绩计算方式不同，
    所以把成绩相关方法定义为抽象方法。
    """

    def __init__(self, name, age):
        # 双下划线表示私有属性，体现“封装”
        self.__name = name
        self.__age = age

    # 使用 property 对外提供只读访问
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @abstractmethod
    def comparison_score(self):
        """
        用于学生之间排名的成绩。

        小学生需要乘以2；
        中学生使用语数外总成绩 + 理综成绩。
        """
        pass

    @abstractmethod
    def actual_total_score(self):
        """
        最终输出的真实总成绩。

        小学生不能乘以2。
        """
        pass

    @abstractmethod
    def to_list(self):
        """
        将学生对象转换回原始列表格式。
        """
        pass

    def sort_key(self):
        """
        排序规则：

        1. 比较成绩从高到低
        2. 成绩相同时，年龄从小到大
        3. 年龄也相同时，姓名字典序从小到大
        """

        return (
            -self.comparison_score(),
            self.age,
            self.name
        )


# =========================
# 2. 小学生类
# =========================

class PrimaryStudent(Student):

    def __init__(self, name, age, total_score):
        # 调用父类构造方法
        super().__init__(name, age)

        self.__total_score = total_score

    def comparison_score(self):
        # 小学生参与比较时，成绩乘以2
        return self.__total_score * 2

    def actual_total_score(self):
        # 最终输出时不能乘以2
        return self.__total_score

    def to_list(self):
        return [
            self.name,
            self.age,
            self.__total_score
        ]


# =========================
# 3. 中学生类
# =========================

class MiddleStudent(Student):

    def __init__(
        self,
        name,
        age,
        three_subject_score,
        science_score
    ):
        super().__init__(name, age)

        self.__three_subject_score = three_subject_score
        self.__science_score = science_score

    def comparison_score(self):
        # 中学生比较成绩为两部分成绩之和
        return (
            self.__three_subject_score
            + self.__science_score
        )

    def actual_total_score(self):
        return (
            self.__three_subject_score
            + self.__science_score
        )

    def to_list(self):
        return [
            self.name,
            self.age,
            self.__three_subject_score,
            self.__science_score
        ]


# =========================
# 4. 根据数据创建对应学生
# =========================

def create_student(data):
    """
    长度为3：
        [姓名, 年龄, 总成绩]
        表示小学生

    长度为4：
        [姓名, 年龄, 语数外总成绩, 理综成绩]
        表示中学生
    """

    if len(data) == 3:
        return PrimaryStudent(
            data[0],
            data[1],
            data[2]
        )

    elif len(data) == 4:
        return MiddleStudent(
            data[0],
            data[1],
            data[2],
            data[3]
        )

    else:
        raise ValueError(
            "学生数据的长度只能是3或4"
        )


# =========================
# 5. 排序并选取前三名
# =========================

def select_top3(raw_data):
    students = []

    # 把每条原始数据转换成学生对象
    for data in raw_data:
        student = create_student(data)
        students.append(student)

    # 根据统一的排序规则排序
    students.sort(
        key=lambda student: student.sort_key()
    )

    # 选出前三名
    top3 = students[:3]

    return students, top3


# =========================
# 6. 测试
# =========================

raw_data = [
    ['zhang3', 10, 90],
    ['li4', 11, 85],
    ['wang5', 12, 88, 92],
    ['zhao6', 13, 95, 89]
]

all_students, top3_students = select_top3(raw_data)


# 输出全部排序结果
sorted_result = []

for student in all_students:
    sorted_result.append(student.to_list())

print("全部排序结果：")
print(sorted_result)


# 输出前三名姓名和真实总成绩
top3_result = []

for student in top3_students:
    top3_result.append([
        student.name,
        student.actual_total_score()
    ])

print("Top 3 姓名和总成绩：")
print(top3_result)