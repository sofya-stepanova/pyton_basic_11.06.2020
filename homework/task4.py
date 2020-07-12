class ValidateError(Exception):
    def __init__(self, message):
        self.message = message


class WareHouse:
    def __init__(self, country, city):
        self.country = country
        self.city = city

        self.office_equip_dict = {}

    def add_to_warehouse(self, *args):
        for equip in args:
            if isinstance(equip, OfficeEquipment):
                original_vars = vars(equip)
                temp_copy_vars = original_vars.copy()
                copy_flag = False
                name = temp_copy_vars.pop('name')
                number = temp_copy_vars.pop('number')

                if name in self.office_equip_dict.keys():
                    for dict_rec in self.office_equip_dict[name]:
                        temp_dict = dict_rec.copy()
                        temp_dict.pop('number')

                        if temp_copy_vars == temp_dict:
                            dict_rec['number']['склад'] += number
                            copy_flag = not copy_flag

                            break

                    if not copy_flag:
                        temp_copy_vars.update({"number": {"склад": number}})
                        self.office_equip_dict[name].append(temp_copy_vars)

                else:
                    temp_copy_vars.update({"number": {"склад": number}})
                    self.office_equip_dict.update({name: [temp_copy_vars]})

    def add_to_unit(self, unit, *args):
        for equip in args:
            if isinstance(equip[0], OfficeEquipment):
                equip_vars = vars(equip[0])
                number = equip[1]
                temp_equip_vars = equip_vars.copy()
                temp_equip_vars.pop('number')
                temp_equip_vars.pop('name')

                if equip_vars['name'] in self.office_equip_dict:
                    for dict_rec in self.office_equip_dict[equip_vars['name']]:
                        temp_dict_rec = dict_rec.copy()
                        temp_dict_rec.pop('number')

                        if temp_equip_vars == temp_dict_rec:
                            if not unit in dict_rec['number']:
                                dict_rec['number'].update({unit: 0})
                            try:
                                if not (dict_rec['number']['склад'] - number > 0):
                                    raise ValidateError(
                                         f"Недостаточно экземпляров {equip_vars['name']} с характеристиками "
                                         f"{temp_equip_vars} на складе для передачи в подразделение!")
                                dict_rec['number'][unit] += number
                                dict_rec['number']['склад'] -= number

                            except ValidateError as e:
                                print(e)

                            break

                        else:
                            continue

    def get_all_equip(self):
        return self.office_equip_dict


class OfficeEquipment:
    def __init__(self, count, dimensions):
        self.count = count
        self.dimensions = dimensions


class Computer(OfficeEquipment):
    def __init__(self, brand, os):
        self.brand = brand
        self.os = os



class Printer(OfficeEquipment):
    def __init__(self, colour_printing, copy):
        self.colour_printing = colour_printing
        self.copy = copy


class Fax(OfficeEquipment):
    def __init__(self, memory, multyadress):
        self.memory = memory
        self.multyadress = multyadress




