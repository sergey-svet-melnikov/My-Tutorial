### Задание №1 - Подготовка рабочей среды

 - Terraform: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.tf.png?raw=true)
 - Bash: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology%20SH.png?raw=true)
 - Markdown: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.md.png?raw=true)
 - Yaml: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.yaml.png?raw=true)
 - Jsonnet: ![](https://github.com/sergey-svet-melnikov/My-Tutorial/blob/main/DevOps-22/Home_Work/01-intro-01/img/Sergey%20Melnikov%20netology.jsonnet.png?raw=true)

### Задание №2 - Описание жизненного цикла задачи

10 Входящая (Задача) от [Заказчика];

20 [Менеджер проекта] взаимодействует и согласовывает все аспекты с [Заказчиком] при необходимости формирует (Задачу на изменение);

30 ЕСЛИ (Задача на изменения) новая ТО [50] ИНАЧЕ 
    ЕСЛИ есть замечания по (Задаче на изменение) со стороны [Менеджера проекта] ИЛИ необходимо отменить ранее сделанные изменения по (Задаче на изменения) ТО [60] ИНАЧЕ [90]

50 Создание (Тестовой среды) [DevOps] для (Задачи на изменение) 

60 Внесение изменений, доработка или отмена (Задачи на изменение) [Программистом]

70 Тестирование изменений по (Задаче на изменения) [Тестировщиком]

80 ЕСЛИ нет замечаний со стороны [Тестировщика] ТО [20] ИНАЧЕ [60]

90  [Программист] или/и [DevOps] выводит задачу в продакшн 

100 [DevOps] демонтирует (Тестовую среду)   
