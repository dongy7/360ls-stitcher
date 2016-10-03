"""
Creates Configuration object based on profile.yml
"""

import os.path
import sys
import yaml

class Configuration(object):
    """ The Configuration class enables configuration instances to be created. """

    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        """ The Configuration class constructor instantiates the Configuration class. """

        self.config_file = "config/profile.yml"
        self.check_config_file()
        self.initialize()

    def check_config_file(self):
        """ Checks for an existing yml configuration file. """

        if not os.path.isfile(self.config_file):
            raise ValueError('Configuration file does not exist.')

    def initialize(self):
        """ Parses profile.yml to initialize configuration values """

        with open(self.config_file, 'r') as config_file:
            doc = yaml.load(config_file)
            self.left_index = self.get_field("left-index", doc)
            self.right_index = self.get_field("right-index", doc)
            self.source_dir = self.get_field("source-dir", doc)
            self.dest_dir = self.get_field("dest-dir", doc)
            self.keyframe = self.get_field("key-frame", doc)
            self.width = self.get_field("width", doc)
            self.format = self.get_field("format", doc)
            self.left_video = self.get_field("left-video", doc)
            self.right_video = self.get_field("right-video", doc)
            self.video_dir = self.get_field("video-dir", doc)
            self.port = self.get_field("port", doc)

    def get_field(self, key, doc):
        """ Checks to make sure valid keys are in the profile.yml configuration file. """
        if key in doc:
            return doc[key]
        else:
            print "\"{0}\" is not a valid key in {1}.".format(key, self.config_file)
            print "Run configure.py again or define key in {0}".format(self.config_file)
            sys.exit(1)