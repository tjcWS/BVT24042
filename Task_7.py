class Employee():
    def __init__(self, name, idd):
        self.name = name
        self.id = idd

    def get_info(self):
        return "Имя: {} \n id: {}".format(self.name, self.id)

print('############################# 1 ########################################')
obj = Employee('Deny', '1882965')
print(obj.get_info())
print('############################# 2 ########################################')

class Manager(Employee):
    def __init__(self, name, idd, department):
        Employee.__init__(self, name, idd)
        self.department = department #отдел 
    def manager_project(self, project):
        self.project = project
        return "Руководитель проекта '{}': {} ({}, отдел: {})".format(self.project, self.name, self.id, self.department)

new_obj = Manager('Deny', '1882965', 'Инженерный')
print(new_obj.manager_project('Link Market'))
print('############################# 3 ########################################')

class Technical():
    def __init__(self, specialization):
        self.specialization = specialization
    def perform_maintenance(self, status):
        if status == 'В процессе' or status == 'Завершен' or status == 'Принят':
            self.status = status
            return "Статус работы: {}".format(self.status)

new_obj_1 = Technical('Разработка чертежа продукта')
print(new_obj_1.perform_maintenance('В процессе'))
print('############################# 4 ########################################')

class TechManager(Manager, Technical):
    def __init__(self, idd, specialization, department):
        super().__init__(self, idd, department)
        Technical.__init__(self, specialization)
        self.employee = []
        self.team_info = {}
    def chek_skills(self, skills):
        if ('более одного года' in skills) or ('работал на' in skills) or ('большое портфолио' in skills):
            self.skills = skills
            return 'Сотрудник подходит'
        else:
            self.skills = None
            return 'У сотрудника слишком маленький опыт'
        
    def set_to_proj(self, set_project):
        if self.skills != None:
            self.set_project = set_project
            return 'Вам назначен новый проект: {}'.format(self.set_project)
        else:
            self.set_project = None
            return 'Проект: не назначен'
        
    def status_of_project(self, status):
        if self.set_project != None:
            if status == 'В процессе' or status == 'Завершен' or status == 'Принят':
                self.status = status
                return "Статус работы: {}".format(self.status)
            
    def check_status(self):
        return 'id: {}\nСпециализация: {}\nОпыт: {}\nОтдел: {}\nПроект: {}\nСтатус: {}'.format(self.id, self.specialization, self.skills, self.department, self.set_project, self.status)\
            
    def add_employee(self, name, id):
        self.employee.append((name, id))
        return self.employee

    def get_team_info(self):
        self.team_info[self.id] = [self.specialization, self.skills, self.department, self.set_project, self.status]
        return self.team_info

tech_obj = TechManager('1882965', 'Разработка', 'Инженерный')
print(tech_obj.chek_skills('Опыт работы более одного года. Имею большое портфолио, работал на компанию Яндекс около 2 лет'))
print(tech_obj.set_to_proj('LM'))
print(tech_obj.status_of_project('Принят'))
print(tech_obj.check_status())
print('############################# 5 ########################################')
print(tech_obj.add_employee('Вася', 1882965))
print(tech_obj.add_employee('Олег', 1773648))
print('############################# 6 ########################################')
team_obj = TechManager('1773648', 'БД', 'Аналитический')
team_obj.chek_skills('Имею опыт работы более одного года')
team_obj.set_to_proj('VKM')
team_obj.status_of_project('Завершен')
team_obj.check_status()

print(tech_obj.get_team_info())
print(team_obj.get_team_info())