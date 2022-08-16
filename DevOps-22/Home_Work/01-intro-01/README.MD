### Задание №1 - Подготовка рабочей среды

 - Terraform: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.tf.png?raw=true)
 - Bash: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology%20SH.png?raw=true)
 - Markdown: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.md.png?raw=true)
 - Yaml: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.yaml.png?raw=true)
 - Jsonnet: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.jsonnet.png?raw=true)

### Задание №2 - Описание жизненного цикла задачи

10 Входящая Задача от [Заказчика]

20 [Менеджер проекта] взаимодействует с [Заказчиком]

30 ЕСЛИ Задача новая ИЛИ есть замечания со стороны [Заказчика] ТО [50] ИНАЧЕ
        ЕСЛИ Задача проверена [Тестировщиком] и нет замечаний со стороны [Менеджера проекта] ТО [110] ИНАЧЕ [80]
    
50 Постановка задачи [Программисту]

60 ЕСЛИ задача не требует создание среды тестирования ТО [80]

70 Создание тестовой среды [DevOps]

80 Внесение изменений [Программистом]

90 Тестирование изменений [Тестировщиком]

100 ЕСЛИ нет замечаний со стороны [Тестировщика] ТО [20] ИНАЧЕ [80]

110 Согласование с [Заказчиком]

120 ЕСЛИ есть замечания со стороны заказчика