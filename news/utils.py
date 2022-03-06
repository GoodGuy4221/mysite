class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, obj):
        if isinstance(obj, str):
            return obj.upper()
        return obj.title.upper()
