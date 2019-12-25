#
#  Author: Adam Jakab
#  Copyright: Copyright (c) 2019., Adam Jakab
#  License: See LICENSE.txt
#  Email: adaja at itu dot dk
#

from importlib import import_module


class ClassLoader:

    @staticmethod
    def import_module(module_path):
        try:
            module = import_module(module_path)
            return module
        except (ImportError, AttributeError) as e:
            raise ImportError("Error importing module: {0}".format(module_path))

    def get_class(self, module_path, class_name):
        module = self.import_module(module_path)
        try:
            klass = getattr(module, class_name)
            return klass
        except (ImportError, AttributeError) as e:
            raise ImportError("Error finding class: {0}".format(class_name))

    def get_instance(self, module_path, class_name, **kwargs):
        klass = self.get_class(module_path, class_name)
        try:
            instance = klass(**kwargs)
            return instance
        except (ImportError, AttributeError) as e:
            raise ImportError("Error finding class: {0}".format(class_name))

