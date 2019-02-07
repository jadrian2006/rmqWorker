#!/usr/bin/env python

import sys
import os
import patoolib as Pat
import pathlib
from extensions import valid_input_extensions, valid_output_extensions, bad_strings


class ProcessFile:

    def __init__(self, files):
        self.files = pathlib.Path(files)
        self.movies = []

    def is_movie(self):
        if self.files.suffix.lower()[1:] in valid_input_extensions or self.files.suffix.lower()[1:] in valid_output_extensions:
            good_file = True
            for strings in bad_strings:
                if str(self.files).lower().find(strings) != -1:
                    good_file = False
            if good_file == True:
                return self.files.is_file()
            else:
                return False
        else:
            return False

    def is_archive(self):
        if self.files.suffix.lower()[1:] in Pat.ArchiveFormats and self.files.suffix.lower()[:1] !='iso':
            good_file = True
            for strings in bad_strings:
                if str(self.files).lower().find(strings) != -1:
                    good_file = False
            if good_file == True:
                return self.files.is_file()
            else:
                return False
        else:
            return False

    def test_archive(self):
        try:
            Pat.test_archive(self.files, verbosity=-1)
            return True
        except:
            return False

    def extract_archive(self,source,outfile):
        pathlib.Path(outfile).mkdir(parents=True, exist_ok=True)    
        try:
            Pat.extract_archive(source, outdir=outfile)
            return True
        except:
            return False

    def find_movie(self):
        self.movies= []
        for files in self.files.iterdir():
            if files.suffix.lower()[1:] in valid_input_extensions or self.files.suffix.lower()[1:] in valid_output_extensions:
                good_file = True
                for strings in bad_strings:
                    if str(self.files).lower().find(strings) != -1:
                        good_file = False
                if good_file == True:
                    self.movies.append(str(files))
        return self.movies


def main():
    log.info('Start')

if __name__=='__main__':
    main()
