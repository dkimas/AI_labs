from pyknow import *

class Professions(KnowledgeEngine):
    @Rule(AND(Fact('Готов к длительному обучению'),Fact('Польза для общества')))      
    def Medicine(self):
        self.declare(Fact('Медицина'))
        
    @Rule(AND(Fact('Медицина'),Fact('Хладнокровие')))
    def surgeon(self):
        self.declare(Fact(profession='Хирург'))

    @Rule(
          AND(Fact('Медицина'),Fact('Умение общаться с детьми')))
    def pediatrician(self):
        self.declare(Fact(profession='Детский врач'))
        
    @Rule(AND(Fact('Медицина'),Fact('Умение водить автомобиль')))
    def ambulancedriver(self):
        self.declare(Fact(profession='Водитель скорой помощи'))
        
    @Rule(Fact('Медицина'),Fact('Умение управлять людьми'))
    def headphysician(self):
        self.declare(Fact(profession='Главврач'))

    @Rule(Fact('Польза для общества'),Fact('Способность обучать других'))
    def teacher(self):
        self.declare(Fact('Преподаватель'))

    @Rule(OR(AND(Fact('Умение общаться с детьми'), Fact('Умение управлять людьми')),
             AND(Fact('Умение общаться с детьми'), Fact('Преподаватель'))))
    def principal(self):
        self.declare(Fact(profession='Директор школы'))

    @Rule(Fact('Умение водить автомобиль'),
          Fact('Преподаватель'))
    def drivingteacher(self):
        self.declare(Fact(profession='Учитель по вождению'))

    @Rule(Fact('Умение общаться с детьми'),
          Fact('Преподаватель'))
    def schoolteacher(self):
        self.declare(Fact(profession='Школьный учитель'))

    @Rule(Fact('Преподаватель'),
          Fact('Знание математики'))
    def mathteacher(self):
        self.declare(Fact(profession='Учитель математики'))

    @Rule(Fact('Преподаватель'),
          Fact('Навыки борьбы'))
    def wrestlingcoach(self):
        self.declare(Fact(profession='Тренер по борьбе'))
        
    @Rule(Fact('Преподаватель'),
          Fact('Филологическое образование'))
    def ruteacher(self):
        self.declare(Fact(profession='Учитель русского языка'))
        
    @Rule(Fact('Преподаватель'),
          Fact('Знание английского языка'))
    def engteacher(self):
        self.declare(Fact(profession='Учитель английского языка'))
        
    @Rule(Fact('Знание английского языка'),
          Fact('Умение работать с клиентами'))
    def translator(self):
        self.declare(Fact(profession='Переводчик'))
           
    @Rule(Fact('Польза для общества'),
          Fact('Опасная работа'))
    def firefighter(self):
        self.declare(Fact(profession='Пожарный'))
        
    @Rule(Fact('Готов к длительному обучению'),
          Fact('Опасная работа'))
    def rescuer(self):
        self.declare(Fact(profession='Спасатель'))
        
    @Rule(Fact('Польза для общества'),
          Fact('Умение стрелять'))
    def police(self):
        self.declare(Fact('Полиция'))
        
    @Rule(Fact('Опасная работа'),
          Fact('Полиция'))
    def policeman(self):
        self.declare(Fact(profession='Полицейский'))
        
    @Rule(Fact('Полиция'),
          Fact('Аналитические навыки'))
    def detective(self):
        self.declare(Fact(profession='Детектив'))
        
    @Rule(Fact('Полиция'),
          Fact('Умение рисовать'))
    def composer(self):
        self.declare(Fact(profession='Составитель фотороботов'))
        
    @Rule(Fact('Навыки борьбы'),
          Fact('Умение стрелять'),
          Fact('Без высшего образования'))
    def securityguard(self):
        self.declare(Fact(profession='Охранник'))
        
    @Rule(Fact('Без высшего образования'),
          Fact('Хорошая физическая подготовка'))
    def courier(self):
        self.declare(Fact(profession='Курьер'))
        
    @Rule(Fact('Большая зарплата'),
          Fact('Хорошая физическая подготовка'))
    def sportsman(self):
        self.declare(Fact('Спортсмен'))
        
    @Rule(Fact('Навыки борьбы'),
          Fact('Спортсмен'))
    def wrestler(self):
        self.declare(Fact(profession='Борец'))
        
    @Rule(Fact('Спортсмен'),
          Fact('Опасная работа'))
    def hockeyplayer(self):
        self.declare(Fact(profession='Хокеист'))
        
    @Rule(Fact('Умение рисовать'),
          Fact('Умение работать с клиентами'))
    def designer(self):
        self.declare(Fact(profession='Дизайнер'))
        
    @Rule(Fact('Спортсмен'),
          Fact('Способность обучать других'))
    def coach(self):
        self.declare(Fact(profession='Тренер'))
        
    @Rule(Fact('Большая зарплата'),
          Fact('Умение управлять людьми'))
    def manager(self):
        self.declare(Fact(profession='Менеджер'))
        
    @Rule(Fact('Умение управлять людьми'),
          Fact('Умение готовить'))
    def headchef(self):
        self.declare(Fact(profession='Шеф-повар'))
        
    @Rule(Fact('Работа во власти'),
          Fact('Большая зарплата'))
    def clerk(self):
        self.declare(Fact(profession='Чиновник'))
        
    @Rule(Fact('Работа во власти'),
          Fact('Знание английского языка'),
          Fact('Путешествия'))
    def diplomat(self):
        self.declare(Fact(profession='Дипломат'))
        
    @Rule(Fact('Хорошая физическая подготовка'),
          Fact('Преподаватель'))
    def FEteacher(self):
        self.declare(Fact(profession='Учитель физкультуры'))
        
    @Rule(Fact('Знание физики'),
          Fact('Преподаватель'))
    def Physteacher(self):
        self.declare(Fact(profession='Учитель физики'))
        
    @Rule(Fact('Знание химии'),
          Fact('Преподаватель'))
    def Chemteacher(self):
        self.declare(Fact(profession='Учитель химии'))
        
    @Rule(Fact('Знание биология'),
          Fact('Преподаватель'))
    def Bioteacher(self):
        self.declare(Fact(profession='Учитель биология'))
    
    @Rule(Fact('Медицина'),
          Fact('Умение работать с клиентами'))
    def apothecary(self):
        self.declare(Fact(profession='Аптекарь'))
    
    @Rule(Fact('Научные исследования'),
          Fact('Знание физики'))
    def physicist(self):
        self.declare(Fact(profession='Физик'))
    
    @Rule(Fact('Научные исследования'),
          Fact('Знание математики'))
    def mathematician(self):
        self.declare(Fact(profession='Математик'))
    
    @Rule(Fact('Научные исследования'),
          Fact('Знание химии'))
    def chemist(self):
        self.declare(Fact(profession='Химик'))
        
    @Rule(Fact('Научные исследования'),
          Fact('Знание биологии'))
    def biologist(self):
        self.declare(Fact(profession='Биолог'))
        
    @Rule(OR(AND(Fact('Медицина'), Fact('Биолог')),
             AND(Fact('Медицина'), Fact('Химик'))))
    def Drugdeveloper(self):
        self.declare(Fact(profession='Разработчик лекарств'))
        
    @Rule(OR(AND(Fact('Работа с компьютером'), Fact('Знание математики')),
             AND(Fact('Работа с компьютером'), Fact('Работа из дома'))))
    def Programmer(self):
        self.declare(Fact(profession='Программист'))
    
    @Rule(Fact('Работа с компьютером'),
          Fact('Без высшего образования'))
    def Accountant(self):
        self.declare(Fact(profession='Бухгалтер'))
        
    @Rule(OR(AND(Fact('Программист'), Fact('Креативность')),
             AND(Fact('Программист'), Fact('Умение рисовать'))))
    def Gamedeveloper(self):
        self.declare(Fact(profession='Разработчик игр'))
    
    @Rule(Fact('Физик'),
          Fact('Креативность'))
    def Engineer(self):
        self.declare(Fact(profession='Инженер'))
        
    @Rule(OR(AND(Fact('Умение рисовать'), Fact('Креативность')),
             AND(Fact('Работа из дома'), Fact('Умение рисовать'))))
    def Artist(self):
        self.declare(Fact(profession='Художник'))
        
    @Rule(Fact('Научные исследования'),
          Fact('Умение управлять людьми'))
    def Rector(self):
        self.declare(Fact(profession='Ректор'))
   
    @Rule(Fact('Умение готовить'),
          Fact('Путешествия'))
    def Cook(self):
        self.declare(Fact(profession='Кок'))
    
    @Rule(Fact('Аналитические навыки'),
          Fact('Знание математики'))
    def Financialanalyst(self):
        self.declare(Fact(profession='Финансовый аналитик'))
    
    @Rule(Fact('Журналисткое образование'),
          Fact('Креативность'))
    def Journalist(self):
        self.declare(Fact(profession='Журналист'))
    
    @Rule(Fact('Журналисткое образование'),
          Fact('Спортсмен'))
    def sportsjournalist(self):
        self.declare(Fact(profession='Спортивный журналист'))
    
    @Rule(Fact('Журналисткое образование'),
          Fact('Опасная работа'))
    def warcorrespondent(self):
        self.declare(Fact(profession='Военный корреспондент'))
    
    @Rule(Fact('Большая зарплата'),
          Fact('Знание математики'))
    def Banker(self):
        self.declare(Fact(profession='Банкир'))
        
    @Rule(Fact('Юридическое образование'),
          Fact('Работа во власти'))
    def prosecutor(self):
        self.declare(Fact(profession='Прокурор'))
        
    @Rule(Fact('Юридическое образование'),
          Fact('Умение работать с клиентами'))
    def jurist(self):
        self.declare(Fact(profession='Юрист'))
        
    @Rule(Fact('Юридическое образование'),
          Fact('Полиция'))
    def Lawyer(self):
        self.declare(Fact(profession='Адвокат'))
    
    @Rule(Fact('Программист'),
          Fact('Аналитические навыки'))
    def Backend(self):
        self.declare(Fact(profession='Backend разработчик'))
    
    @Rule(Fact('Работа во власти'),
          Fact('Харизма'))
    def Politician(self):
        self.declare(Fact(profession='Политик'))
    
    @Rule(Fact('Умение готовить'),
          Fact('Харизма'))
    def Cookingshow(self):
        self.declare(Fact(profession='Ведущий кулинарного шоу'))
    
    @Rule(Fact('Работа с клиентами'),
          Fact('Путешествия'))
    def Stewardess(self):
        self.declare(Fact(profession='Стюардесса'))
        
    @Rule(Fact('Умение управлять самолётом'))
    def Civilpilot(self):
        self.declare(Fact(profession='Гражданский лётчик'))
        
    @Rule(Fact('Умение управлять самолётом'),
          Fact('Хорошая физическая подготовка'))
    def Astronaut(self):
        self.declare(Fact(profession='Космонавт'))
        
    @Rule(Fact('Умение управлять самолётом'),
          Fact('Опасная работа'))
    def Militarypilot(self):
        self.declare(Fact(profession='Военный лётчик'))
    
    @Rule(Fact('Путешествия'),
          Fact('Опасная работа'))
    def Sailor(self):
        self.declare(Fact(profession='Моряк'))
        
    @Rule(Fact('Умение водить автомобиль'),
          Fact('Без высшего образования'))
    def Taxidriver(self):
        self.declare(Fact(profession='Таксист'))
    
    @Rule(Fact('Актёрские навыки'),
          Fact('Харизма'))
    def TVshow(self):
        self.declare(Fact(profession='Ведущий телешоу'))
        
    @Rule(Fact('Актерские навыки'),
      Fact('Большая зарплата')) 
    def actor(self):
        self.declare(Fact(profession='Актер'))
    
    @Rule(Fact('Умение водить авто'),
          Fact('Большая зарплата')) 
    def driver(self):
        self.declare(Fact(profession='Частный водитель'))
    
    @Rule(Fact('Умение управлять самолетом'),
          Fact('Большая зарплата')) 
    def pilot(self):
        self.declare(Fact(profession='Частный летчик'))
    
    @Rule(Fact('Актреские навыки'),
          Fact('Путешесвия')) 
    def touringactor(self):
        self.declare(Fact(profession='Гастролирующий актер'))
    
    @Rule(Fact('Умение петь'),
          Fact('Большая зарплата')) 
    def singer(self):
        self.declare(Fact(profession='Певец'))
    
    @Rule(Fact('Работа во власти'),
          Fact('Опасная работа')) 
    def bodyguard(self):
        self.declare(Fact(profession='Телохранитель'))
    
    @Rule(Fact('Актреские навыки'),
          Fact('Ораторские навыки')) 
    def voiceactor(self):
        self.declare(Fact(profession='Актер озвучки'))
    
    @Rule(Fact('Актреские навыки'),
          Fact('Опасная работа')) 
    def circusperformer(self):
        self.declare(Fact(profession='Циркач'))
    
    @Rule(Fact('Харизма'),
          Fact('Ораторские навыки'))
    def radiohost(self):
        self.declare(Fact(profession='Радиоведущий'))
    
    @Rule(Fact('Креативность'),
          Fact('Умение управлять людьми')) 
    def director(self):
        self.declare(Fact(profession='Режиссер'))
    
    @Rule(Fact('Актреские навыки'),
          Fact('Умение управлять самолетом')) 
    def airshow(self):
        self.declare(Fact(profession='Участник аэрошоу'))
    
    @Rule(Fact('Харизма'),
          Fact('Способность обучать других')) 
    def coach(self):
        self.declare(Fact(profession='Тренер'))
    
    @Rule(Fact('Полиция'),
          Fact('Химик')) 
    def criminologist(self):
        self.declare(Fact(profession='Криминалист'))
    
    @Rule(Fact('Ораторские навыки'),
          Fact('Работа во власти')) 
    def newscaster(self):
        self.declare(Fact(profession='Ведущий новостей'))
    
    @Rule(Fact('Креативность'),
          Fact('Умение работать с клиентами'),
          Fact('Умение стричь'))
    def hairdresser(self):
        self.declare(Fact(profession='Парикмахер'))
    
    @Rule(Fact('Актерские навыки'),
          Fact('Умение работать с детьми'))
    def childrenactor(self):
        self.declare(Fact(profession='Актер детского театра'))
    
    @Rule(OR(AND(Fact('Умение работать с детьми'), Fact('Харизма')),
     AND(Fact('Умение работать с детьми'), Fact('Ораторские навыки'))))
    def childrenhost(self):
        self.declare(Fact(profession='Ведущий детских шоу'))
    
    @Rule(Fact('Способность обучать других'),
          Fact('Умение ладить с собакими')) 
    def cynologist(self):
        self.declare(Fact(profession='Кинолог'))
    
    @Rule(Fact('Способность обучать других'),
          Fact('Умение ладить с собакими'))
    def cynologist(self):
        self.declare(Fact(profession='Кинолог'))
    
    @Rule(Fact('Актерские навыки'),
          Fact('Умение петь')) 
    def actormusical(self):
        self.declare(Fact(profession='Актер мюзикла'))
    
    @Rule(Fact('Без высшего образования'),
          Fact('Харизма'),
          Fact('Умение работать с клиентами'))
    def seller(self):
        self.declare(Fact(profession='Продавец'))
    
    @Rule(Fact('Большая зарплата'),
          Fact('Умение готовить')) 
    def privatechef(self):
        self.declare(Fact(profession='Частный повар'))
    
    @Rule(Fact('Медицина'),
          Fact('Большая зарпата')) 
    def privatedoctor(self):
        self.declare(Fact(profession='Частный врач'))
    
    @Rule(Fact('Без высшего образования'),
          Fact('Ораторские навыки'),
          Fact('Умение работать с клиентами'))
    def callcenteremployee(self):
        self.declare(Fact(profession='Работник колл-центра'))
    
    @Rule(Fact('Без высшего образования'),
          Fact('Познания в еде'),
          Fact('Умение работать с клиентами'))
    def waiter(self):
        self.declare(Fact(profession='Официант'))
    
    @Rule(Fact('Познания в еде'),
          Fact('Большая зарплата'))
    def sommelier(self):
        self.declare(Fact(profession='Сомелье'))
    
    @Rule(Fact('Преподаватель'),
          Fact('Знание истории'))
    def historyteacher(self):
        self.declare(Fact(profession='Учитель истории'))
    
    @Rule(Fact('Научные исследования'),
          Fact('Знание истории'))
    def historian(self):
        self.declare(Fact(profession='Историк'))
    
    @Rule(Fact('Путешествия'),
          Fact('Знание истории'))
    def archaeologist(self):
        self.declare(Fact(profession='Археолог'))
    
    @Rule(Fact('Преподаватель'),
          Fact('Актерские навыки'))
    def actingteacher(self):
        self.declare(Fact(profession='Преподаватель актерского мастерства'))
    
    @Rule(Fact('Креативность'),
          Fact('Умение пользоваться компьютером'))
    def creatorspecialeffects(self):
        self.declare(Fact(profession='Создатель спецэффектов'))
    
    @Rule(Fact('Харизма'),
          Fact('Знание истории'))
    def hosthistoricalprogram(self):
        self.declare(Fact(profession='Ведущий исторической передачи'))
   
    @Rule(OR(AND(Fact('Харизма'), Fact('Знание физики')),
         AND(Fact('Харизма'), Fact('Знание биологии'))))
    def hostscientificprogram(self):
        self.declare(Fact(profession='Ведущий научно-популярной передачи'))
    
    @Rule(Fact('Без высшего образования'),
          Fact('Грязная работа'))
    def cleaner(self):
        self.declare(Fact(profession='Уборщик'))
    
    
    @Rule(Fact(profession=MATCH.a))
    def print_result(self,a):
          print('Профессия - {}'.format(a))
                    
    def factz(self,l):
        for x in l:
            self.declare(x)
