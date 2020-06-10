def add_steps(item: dict):
    if 'sourceDetails' not in item or 'url' not in item['sourceDetails'] \
            or 'url' not in item['sourceDetails']:
        return item

    item['sourceDetails']['steps'] = f'''Realiza los siguientes pasos para obtener más información acerca de la convocatoria:
            \n 1. Ingresa el portal de becas del [ICETEX]({item['sourceDetails']["url"]})
            \n 2. Selecciona la opción _Número de Convocatoria_
            \n 3. Ingresa el siguiente número: **{item['sourceDetails']["id"]}**
            \n 4. Presiona en _Buscar_'''

    return item
