import random
import tkinter



class Bee:  # Super class bee
    def __init__(self, age_days, weight, number=0):
        self.weight = weight
        self.age_days = age_days
        self.number = number
        # 0 - Живая; 1 - Состарилась; 2 - Умерла от голода;
        self.cause_death = 0

    def get_weight(self):
        return self.weight

    def consume_honey(self):
        eat_or_uneat = random.randint(0, 100)
        if eat_or_uneat >= 5:
            return self.weight * 0.1
        else:
            self.cause_death = 2
            return False

    def get_cause_death(self):
        return self.cause_death

    def get_number(self):
        return self.number

    def grow_up(self):
        self.age_days += 1
        return self.age_days

    def check_life(self):
        if self.cause_death == 1:
            return False
        elif self.age_days > 60:
            self.cause_death = 1
            return False
        else:
            return True


class WorkBee(Bee):
    def __init__(self, weight, number, age_days, col_honey):
        self.col_honey = col_honey
        super().__init__(age_days, weight, number)

    def collect_honey(self):
        return self.col_honey

    def check_activity(self):
        bee_activity = random.randint(0, 100)
        if bee_activity > 20:
            return True
        else:
            return False

    def __str__(self):
        return 'Номер пчелы: {}'.format(self.number)


class UnworkBee(Bee):
    def __init__(self, weight, number, age_days):
        super().__init__(age_days, weight, number)

    def fertilization(self):
        return 10
        # return random.randint(10, 15)


class MotherBee(Bee):
    def __init__(self, weight, number, age_days):
        super().__init__(age_days, weight, number)

    def sowing(self):
        return random.randint(100, 150)


class Larva:
    def __init__(self, number):
        # через 9 дней вырастает
        self.number = number
        self.day_age = 0

    def eat_honey(self):
        eating = random.randint(0, 100)
        if eating > 5:
            return 0.5
        else:
            return False

    def growup_larva(self):
        self.day_age += 1

    def age_larva(self):
        return self.day_age

    def __str__(self):
        return 'Number {} Возраст {}'.format(self.number, self.day_age)


class Egg:
    def __init__(self, number):
        self.number = number
        self.day_egg_life = 0 # после 2 дней жизни умерает

    def day_life(self):
        self.day_egg_life +=1

    def __str__(self):
        return 'Яйцо номер: {}'.format(self.number)



class Hive:
    def __init__(self, honey_hive):
        self.quantity_cleanup_bees = None
        self.honey_hive = honey_hive
        self.day = 0
        self.bee = []
        self.egg = []
        self.larva = []
        self.die_bee = 0
        self.number_larva = 0
        self.number_bee = 0

    def count_die_bees(self):
        die_bee = 0
        for bee in self.bee:
            if bee.cause_death != 0:
                die_bee += 1
        return print('Количество мертвых, не выметенных пчел: ', die_bee)

    def add_bee(self, bee):
        self.number_bee += 1
        self.bee.append(bee)

    def get_number_bee(self):
        return self.number_bee

    def life(self):
        arr_activity_cleaning_bee = []  # пчёлы занимающиеся уборкой мёда
        arr_activity_collect_bee = []  # пчёлы занимаающиеся сбором мёда

        collect_honey_bee_day = 0  # кол-во меда съеденого за день
        eaten_honey_day = 0  # кол-во меда съеденого за день
        quantity_work_bee = 0  # кол-во рабочих пчел
        quantity_unwork_bee = 0  # кол-во трутней
        count_bees_die_hunger = 0  # кол-во пчёл умирающих от голода
        count_bees_die_age = 0  # кол-во пчёл умирающих от старости
        count_unworkbee_die_age = 0  # кол-во туртней умирающих от возраста
        count_unworkbee_die_hunger = 0  # кол-во трутней умирающих от голода

        self.day += 1
        print('Day: {}'.format(self.day))

        for bee in self.bee:
            # condition for honey
            if bee.check_life():
                if type(bee) == MotherBee:
                    self.egg += [Egg(i) for i in range(bee.sowing())]
                if type(bee) == WorkBee:
                    quantity_work_bee += 1
                    if bee.consume_honey() and bee.get_cause_death() == 0:
                        self.honey_hive -= bee.consume_honey()
                        eaten_honey_day += bee.consume_honey()
                        if bee.check_activity():
                            arr_activity_collect_bee.append(bee)
                            self.honey_hive += bee.collect_honey()
                            collect_honey_bee_day +=bee.collect_honey()
                            print('Рабочая пчела номер {} занимается сбором меда'.format(bee.get_number()))
                        else:
                            arr_activity_cleaning_bee.append(bee)
                            print('Рабочая пчела номер {} занимается уборкой пчел'.format(bee.get_number()))
                    else:
                        print('Рабочая пчела номер {} умерла от голода'.format(bee.get_number()))
                        count_bees_die_hunger += 1
                else:
                    quantity_unwork_bee += 1
                if type(bee) == UnworkBee:
                    if bee.get_cause_death() == 0:
                        print('Трутень номер {} жив'.format(bee.get_number()))
                    if bee.get_cause_death() == 2:
                        print('Трутень номер {} умер от голода'.format(bee.get_number()))
                        count_unworkbee_die_hunger += 1
            else:
                if type(bee) == WorkBee:
                    print('Рабочая пчела номер {} состарилась'.format(bee.get_number()))
                    count_bees_die_age += 1
                elif type(bee) == UnworkBee:
                    print('Трутень номер {} состарилась'.format(bee.get_number()))
                    count_unworkbee_die_age += 1

            bee.grow_up()  # bee growth

        for bee in self.bee:
            if type(bee) == UnworkBee:
                for i in range(bee.fertilization()):
                    self.number_larva += 1
                    if not self.egg:
                        break
                    self.egg.remove(self.egg[0])
                    self.larva.append(Larva(self.number_larva))

        count_lar_die_hunger = 0  # кол-во личинок умирающих от голода

        for i, lar in enumerate(self.larva[:]):
            if type(lar.eat_honey()):
                self.honey_hive -= lar.eat_honey()
            else:
                self.larva.remove(lar)
                count_lar_die_hunger += 1

            lar.growup_larva()

            if lar.age_larva() == 9:
                self.number_bee += 1
                choice = random.randint(0, 100)
                if choice > 40:
                    self.bee.append(WorkBee(random.randint(1, 3), self.number_bee, 0, random.randint(3, 4)))
                else:
                    self.bee.append(UnworkBee(random.randint(1, 3), hive.get_number_bee(), random.randint(0, 60)))
                self.larva.remove(lar)

        if not self.larva:
            print('Трутней достаточно')
        else:
            print('Трутней недостаточно\n Количество оставшихся личинок: {}'.format(len(self.larva)))
            print('Количество недостающих трутней: {}'.format(len(self.larva) // 10))

        count_larva_die_age = 0  # кол-во личинок умирающих от возраста

        for lar in self.larva:
            if lar.age_larva() > 9:
                self.larva.remove(lar)
                count_larva_die_age += 1

        count_die_larva = count_larva_die_age + count_lar_die_hunger

        print('Количество личинок: {}'.format(len(self.larva)))

        print()

        print('Количество трутней: {}'.format(quantity_unwork_bee))

        print()

        print('Количество рабочих пчёл: {}'.format(quantity_work_bee))

        print()

        print('Пчелы принесли {} грамм меда'.format(collect_honey_bee_day))

        print(' ')

        print('Пчелы съели {} грамм меда'.format(eaten_honey_day))

        print(' ')

        diff_btw_honey = collect_honey_bee_day - eaten_honey_day  # разница между принесенным медом и съеденным за день

        if diff_btw_honey > 0:
            print('Пчелы пополнили улей на {} грамм меда'.format(
                diff_btw_honey
            ))
        else:
            print('Пчелы уменьшили количество меда в улье на {} грамм'.format(
                (-diff_btw_honey)
            ))

        print(' ')

        quantity_bee_die = count_bees_die_hunger + count_bees_die_age  # кол-во мертвых пчёл

        if quantity_bee_die > 0:
            print('Процент пчел умирающих от голода: {}%'.format(
                (round((count_bees_die_hunger / quantity_bee_die) * 100))
            ))
        else:
            print('Процент пчел умирающих от голода: 0%')

        quantity_die_larva = count_larva_die_age + count_lar_die_hunger  # кол-во мертвых личинок

        if quantity_die_larva > 0:
            print('Процент личинок умирающих от голода: {}%'.format(
                (count_lar_die_hunger / quantity_die_larva) * 100))
        else:
            print('Процент личинок умирающих от голода: 0')

        quantity_unwork_bee = count_unworkbee_die_age + count_unworkbee_die_age

        if quantity_unwork_bee > 0:
            print('Процент трутней умирающих от голода: {}%'.format(
                (count_unworkbee_die_hunger / quantity_unwork_bee) * 100))
        else:
            print('Процент трутней умирающих от голода: 0')

        print(' ')

        for bee in self.bee:
            if type(bee) == UnworkBee:
                for i in range(bee.fertilization()):
                    self.number_larva += 1
                    if not self.egg:
                        break
                    self.egg.remove(self.egg[0])
                    self.larva.append(Larva(self.number_larva))

        print('Количество простаивающих выметающих рабочих пчел:', len(arr_activity_cleaning_bee))

        print(' ')

        # cleaning bees
        for j in self.bee[:]:
            if j.cause_death == 0:
                continue
            for k in arr_activity_cleaning_bee[:]:
                if k.get_weight() >= j.get_weight():
                    self.bee.remove(j)
                    arr_activity_cleaning_bee.remove(k)
                    break

        for bee in self.bee:
            if bee.get_cause_death() != 0:
                self.die_bee += 1

        print('Количество мертвых, не выметенных пчел:', self.die_bee)

        print(' ')

        print('Количество мёда в улье: {}'.format(round(self.honey_hive)))

        for egg in self.egg:
            if egg.day_life() == 2:
                self.egg.remove(egg)


hive = Hive(10000)

mother_bee = MotherBee(3, 1, 1)
hive.add_bee(mother_bee)

#создание рабочих пчёл
for workbee in range(25):
    hive.add_bee(WorkBee(random.randint(1, 3), hive.get_number_bee(), random.randint(0, 60), random.randint(3, 4)))
#создание трутней
for unwork_bee in range(12):
    hive.add_bee(UnworkBee(random.randint(1, 3), hive.get_number_bee(), random.randint(0, 60)))
# жизнь
for i in range(12):
    hive.life()

# hive.life()

