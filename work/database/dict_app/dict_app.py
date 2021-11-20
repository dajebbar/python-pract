class Glob:
    """[space name of variables and functions <pseudo-globals>]
    """
    dbName = 'discotheque' # name of database
    user = 'dajebbar@gmx.fr' # name of user
    passwd = 'purpel' # password of db
    host = '127.0.0.1' # IP adress of server
    port = 5432


    # Database structure. Dictionary of tables and fields

    dicoT = {
        "compositors": [
            ('id_comp', "k", "primary key"),
            ('name', 25, 'name'),
            ('yr_birth', "i", 'year of birth'),
            ('yr_death', "i", 'year of death')

        ],
        "works": [
            ('id_works', "k", "primary key"),
            ('id_comp', "i", "compositor key"),
            ('title', 50, "title of works"),
            ('duration', "i", "duration(min)"),
            ('interpr', 30, "principal interpret")
        ],
    }

