import requests
from utils.misc.next_request import NextRequest
import data.config


def func1(i):
    for _ in range(1, 20):
        yield _
        i += 1


i = func1(1)


def func2(j):
    for _ in range(1, 20):
        yield _
        j += 1


j = func2(1)


def func3(k):
    for _ in range(1, 20):
        yield _
        k += 1


k = func3(1)


def func4(c):
    for _ in range(1, 20):
        yield _
        c += 1


c = func4(1)


class AllCourses:
    header = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Basic dVVNMU5tQVpjb1dOQkthRVJUc2N0d0tMb21kRGI3OFM3VzdKR0JOTTpldHVRWGNUT2lHSVRWWVlmazZKWFB3YklwajZacXd3ZE1hdUxXbDdFQzhwQW5YbVhJUXByUE4wV0hYQ2NaS1VvS1lQcDVGanVtVUJzejkzYkp0ZWFkMkpnSENRSUlvNVNnVTk5RzdTaU9GbnI3eEk2c2xVTzZiOEVOVThlUjEyYw==",
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.url = f"https://www.udemy.com/api-2.0/courses/?page={k.__next__()}&page_size=12&client_id=config.CLIENT_ID&client_secret=config.SECRET_KEY&locale=ru_RU"
        self.header = AllCourses.header
        self.response = requests.get(self.url, headers=self.header)

    def get_courses(self):
        res = self.response.json()

        res = res['results']
        print(res)
        lst = []
        for i in range(12):
            courses = {'title': None, 'url': None, 'author': None, 'lang': None}
            courses['title'] = res[i]['title']
            courses[f'url'] = "https://udemy.com" + res[i]['url']
            courses[f'author'] = res[i]['visible_instructors'][0]["title"]
            courses[f'lang'] = res[i]['locale']['title']
            courses[f'price'] = res[i]['price']
            courses[f'headline'] = res[i]['headline']
            lst.append(courses)

        return lst

    def one_courses(self, i):
        lst = self.get_courses()
        title = lst[i]["title"]
        url = lst[i]['url']
        author = lst[i]['author']
        lang = lst[i]['lang']
        price = lst[i]['price']
        headline = lst[i]['headline']
        print(title, url, author, lang, price, headline)
        return title, url, author, lang, price, headline


class RuCourses:
    header = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Basic dVVNMU5tQVpjb1dOQkthRVJUc2N0d0tMb21kRGI3OFM3VzdKR0JOTTpldHVRWGNUT2lHSVRWWVlmazZKWFB3YklwajZacXd3ZE1hdUxXbDdFQzhwQW5YbVhJUXByUE4wV0hYQ2NaS1VvS1lQcDVGanVtVUJzejkzYkp0ZWFkMkpnSENRSUlvNVNnVTk5RzdTaU9GbnI3eEk2c2xVTzZiOEVOVThlUjEyYw==",
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.url = f"https://www.udemy.com/api-2.0/courses/?page={i.__next__()}&page_size=12&client_id=config.CLIENT_ID&client_secret=config.SECRET_KEY&locale=ru_RU"
        self.header = RuCourses.header
        self.response = requests.get(self.url, headers=self.header)

    def get_courses(self):
        res = self.response.json()
        res = res['results']

        lst = []
        for i in range(12):
            courses = {'title': None, 'url': None, 'author': None, 'lang': None}
            courses['title'] = res[i]['title']
            courses[f'url'] = "https://udemy.com" + res[i]['url']
            courses[f'author'] = res[i]['visible_instructors'][0]["title"]
            courses[f'lang'] = res[i]['locale']['title']
            courses[f'price'] = res[i]['price']
            courses[f'headline'] = res[i]['headline']
            lst.append(courses)
        return lst

    def one_courses(self, i=0):
        lst = self.get_courses()
        title = lst[i]["title"]
        url = lst[i]['url']
        author = lst[i]['author']
        lang = lst[i]['lang']
        price = lst[i]['price']
        headline = lst[i]['headline']
        return title, url, author, lang, price, headline


class EnCourses:
    header = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Basic dVVNMU5tQVpjb1dOQkthRVJUc2N0d0tMb21kRGI3OFM3VzdKR0JOTTpldHVRWGNUT2lHSVRWWVlmazZKWFB3YklwajZacXd3ZE1hdUxXbDdFQzhwQW5YbVhJUXByUE4wV0hYQ2NaS1VvS1lQcDVGanVtVUJzejkzYkp0ZWFkMkpnSENRSUlvNVNnVTk5RzdTaU9GbnI3eEk2c2xVTzZiOEVOVThlUjEyYw==",
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.url = f"https://www.udemy.com/api-2.0/courses/?page={j.__next__()}&page_size=12&client_id=config.CLIENT_ID&client_secret=config.SECRET_KEY&locale=en_EN"
        self.header = EnCourses.header
        self.response = requests.get(self.url, headers=self.header)

    def get_courses(self):
        res = self.response.json()
        res = res['results']

        lst = []
        for i in range(12):
            courses = {'title': None, 'url': None, 'author': None, 'lang': None}
            courses['title'] = res[i]['title']
            courses[f'url'] = "https://udemy.com" + res[i]['url']
            courses[f'author'] = res[i]['visible_instructors'][0]["title"]
            courses[f'lang'] = res[i]['locale']['title']
            courses[f'price'] = res[i]['price']
            courses[f'headline'] = res[i]['headline']
            lst.append(courses)

        return lst

    def one_courses(self, i=1):
        lst = self.get_courses()
        title = lst[i]["title"]
        url = lst[i]['url']
        author = lst[i]['author']
        lang = lst[i]['lang']
        price = lst[i]['price']
        headline = lst[i]['headline']
        return title, url, author, lang, price, headline


class FreeCourses:
    header = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Basic dVVNMU5tQVpjb1dOQkthRVJUc2N0d0tMb21kRGI3OFM3VzdKR0JOTTpldHVRWGNUT2lHSVRWWVlmazZKWFB3YklwajZacXd3ZE1hdUxXbDdFQzhwQW5YbVhJUXByUE4wV0hYQ2NaS1VvS1lQcDVGanVtVUJzejkzYkp0ZWFkMkpnSENRSUlvNVNnVTk5RzdTaU9GbnI3eEk2c2xVTzZiOEVOVThlUjEyYw==",
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.url = f"https://www.udemy.com/api-2.0/courses/?page={c.__next__()}&page_size=12&client_id=config.CLIENT_ID&client_secret=config.SECRET_KEY&locale=en_EN"
        self.header = EnCourses.header
        self.response = requests.get(self.url, headers=self.header)

    def get_courses(self):
        res = self.response.json()
        res = res['results']

        lst = []
        for i in range(12):
            courses = {'title': None, 'url': None, 'author': None, 'lang': None}
            courses['title'] = res[i]['title']
            courses[f'url'] = "https://udemy.com" + res[i]['url']
            courses[f'author'] = res[i]['visible_instructors'][0]["title"]
            courses[f'lang'] = res[i]['locale']['title']
            courses[f'price'] = res[i]['price']
            courses[f'headline'] = res[i]['headline']
            lst.append(courses)

        return lst

    def one_courses(self, i=1):
        lst = self.get_courses()
        title = lst[i]["title"]
        url = lst[i]['url']
        author = lst[i]['author']
        lang = lst[i]['lang']
        price = lst[i]['price']
        headline = lst[i]['headline']
        return title, url, author, lang, price, headline
