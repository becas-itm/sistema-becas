from itm.publishing.domain.scholarship import AcademicLevel


POSTGRADUATE_LEVELS = ['graduates', 'doctoral candidates/phd students',
                       'postdoctoral researchers', 'faculty']


def calculate_academic_level(item: dict):
    if 'academicLevel' not in item:
        return item

    print(111111111111,  get_academic_level(item['academicLevel'].lower()))

    item['academicLevel'] = get_academic_level(item['academicLevel'].lower())

    return item


def get_academic_level(levels):
    if is_undergraduate(levels) and is_postgraduate(levels):
        return AcademicLevel.BOTH.value

    if is_undergraduate(levels):
        return AcademicLevel.UNDERGRADUATE.value

    if is_postgraduate(levels):
        return AcademicLevel.POSTGRADUATE.value

    return AcademicLevel.OTHERS.value


def is_undergraduate(levels):
    if 'undergraduates' in levels:
        return True


def is_postgraduate(levels):
    for level in POSTGRADUATE_LEVELS:
        if level in levels:
            return True
