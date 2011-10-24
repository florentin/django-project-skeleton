import IPython.ipapi
ip = IPython.ipapi.get()


def main():
    imported = "\nImported models:\n\n"

    try:
        from django.db.models.loading import get_models
        for m in get_models():
            try:
                ip.ex("from %s import %s" % (m.__module__, m.__name__))
                imported += "%s.%s\n" % (m.__module__, m.__name__)
            except ImportError:
                print "INFO: could not find a django env"
        print imported
    except ImportError:
        pass


main()

