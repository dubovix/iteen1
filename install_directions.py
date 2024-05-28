from typing import Any

from django.core.management.base import BaseCommand

from api.models import Direction

data = [
    {
        "class_level": "0",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "0",
        "direction_name": "Робототехника",
        "url": "https://iteen.by/programs/"
        "doshkolniki-6-7-let/?DIRECTIONS[]=1479",
    },
    {
        "class_level": "0",
        "direction_name": "Computer science",
        "url": "https://iteen.by/programs/"
        "doshkolniki-6-7-let/?DIRECTIONS[]=5412",
    },
    {
        "class_level": "0",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/"
        "doshkolniki-6-7-let/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "1",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "1",
        "direction_name": "Робототехника",
        "url": "https://iteen.by/programs/1-class/?DIRECTIONS[]=1479",
    },
    {
        "class_level": "1",
        "direction_name": "Computer science",
        "url": "https://iteen.by/programs/1-class/?DIRECTIONS[]=5412",
    },
    {
        "class_level": "2",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "2",
        "direction_name": "Робототехника",
        "url": "https://iteen.by/programs/2-class/?DIRECTIONS[]=1479",
    },
    {
        "class_level": "2",
        "direction_name": "Computer science",
        "url": "https://iteen.by/programs/2-class/?DIRECTIONS[]=5412",
    },
    {
        "class_level": "2",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/2-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "2",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/2-class/",
    },
    {
        "class_level": "3",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "3",
        "direction_name": "Робототехника",
        "url": "https://iteen.by/programs/3-class/?DIRECTIONS[]=1479",
    },
    {
        "class_level": "3",
        "direction_name": "Техномейкерство",
        "url": "https://iteen.by/programs/3-class/?DIRECTIONS[]=1482",
    },
    {
        "class_level": "3",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/3-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "3",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/3-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "3",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/3-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "4",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "4",
        "direction_name": "Робототехника",
        "url": "https://iteen.by/programs/4-class/?DIRECTIONS[]=1479",
    },
    {
        "class_level": "4",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/4-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "4",
        "direction_name": "Техномейкерство",
        "url": "https://iteen.by/programs/4-class/?DIRECTIONS[]=1482",
    },
    {
        "class_level": "4",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/4-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "4",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/4-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "4",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/4-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "5",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "5",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "5",
        "direction_name": "Техномейкерство",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1482",
    },
    {
        "class_level": "5",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "5",
        "direction_name": "Авиамодели_БПЛА",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1503",
    },
    {
        "class_level": "5",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "5",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "6",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "6",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "6",
        "direction_name": "Техномейкерство",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1482",
    },
    {
        "class_level": "6",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "6",
        "direction_name": "Авиамодели_БПЛА",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=1503",
    },
    {
        "class_level": "6",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "6",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/5-6-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "7",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "7",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "7",
        "direction_name": "Техномейкерство",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1482",
    },
    {
        "class_level": "7",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "7",
        "direction_name": "Web-технологии",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1504",
    },
    {
        "class_level": "7",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "7",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "8",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "8",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "8",
        "direction_name": "Техномейкерство",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1482",
    },
    {
        "class_level": "8",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "8",
        "direction_name": "Web-технологии",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=1504",
    },
    {
        "class_level": "8",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "8",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/7-8-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "9",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "9",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "9",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "9",
        "direction_name": "Web-технологии",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=1504",
    },
    {
        "class_level": "9",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "9",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "10",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "10",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "10",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "10",
        "direction_name": "Web-технологии",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=1504",
    },
    {
        "class_level": "10",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "10",
        "direction_name": "Спортивная робототехника",
        "url": "https://iteen.by/programs/9-10-class/?DIRECTIONS[]=13043",
    },
    {
        "class_level": "11",
        "direction_name": "Все направления",
        "url": "https://iteen.by/programs/#",
    },
    {
        "class_level": "11",
        "direction_name": "Дизайн",
        "url": "https://iteen.by/programs/11-class/?DIRECTIONS[]=1480",
    },
    {
        "class_level": "11",
        "direction_name": "Программирование и Game Dev",
        "url": "https://iteen.by/programs/11-class/?DIRECTIONS[]=1484",
    },
    {
        "class_level": "11",
        "direction_name": "Web-технологии",
        "url": "https://iteen.by/programs/11-class/?DIRECTIONS[]=1504",
    },
    {
        "class_level": "11",
        "direction_name": "Computer science",
        "url": "https://iteen.by/programs/11-class/?DIRECTIONS[]=5412",
    },
    {
        "class_level": "11",
        "direction_name": "Экспресс-курсы",
        "url": "https://iteen.by/programs/11-class/?DIRECTIONS[]=8311",
    },
    {
        "class_level": "None",
        "direction_name": "It-лаборатория",
        "url": "None",
    },
]


class Command(BaseCommand):
    """
    Create a table with classes and their directions if there are none.
    Takes args from environment variables.
    """

    def handle(self, *args: Any, **options: Any) -> None:
        if Direction.objects.all().count() != len(data):
            Direction.objects.all().delete()
            for direction_date in data:
                direction_to_save = Direction(
                    class_level=direction_date["class_level"],
                    direction_name=direction_date["direction_name"],
                    url=direction_date["url"],
                )
                direction_to_save.save()

            self.stdout.write("Class Direction installed successfully.")
            return
        self.stdout.write("Direction already exist.")
        return
