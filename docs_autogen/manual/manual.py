from make_real_readme import main


##-#-#-# ##-#-#-#
# Post-process logic
##-#-#-# ##-#-#-#
insert_md_section_for__class_methods = False
remove_repeated_sections_classmethods = False




class BESTLOG(object):
    def __init__(self):
        self.error_list = []
        self.warning_list = []
        self.info_list = []
        self.debug_list = []
        self.tick_amount=1
        self.names = self.messages_names = 'error warning info debug'.split(' ')

    def _tick(self):
        self.tick_amount+=1
        return self.tick_amount

    def error(self, m, metadata={}):
        self.error_list.append([self._tick(), m, metadata])
    def warning(self, m, metadata={}):
        self.warning_list.append([self._tick(), m, metadata])
    def info(self, m, metadata={}):
        self.info_list.append([self._tick(), m, metadata])
    def debug(self, m, metadata={}):
        self.debug_list.append([self._tick(), m, metadata])

    def printout_all(self):
        print("error_list")
        [print("   ", x) for x in self.error_list]
        print("warning_list")
        [print("   ", x) for x in self.warning_list]
        print("info_list")
        [print("   ", x) for x in self.info_list]
        print("debug_list")
        [print("   ", x) for x in self.debug_list]




def compile_index():

    log_obj = BESTLOG()

    main(logger=log_obj,
         main_md_file='docs_autogen/readme/markdown_source_files/2_readme.md',
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[
                'docs_autogen/readme/markdown_source_files/1_HEADER_top_part.md',
                'docs_autogen/readme/markdown_source_files/2_readme.md',
                'docs_autogen/readme/markdown_source_files/3_FOOTER.md',
                'docs_autogen/readme/markdown_source_files/4_Release_notes.md'
             ],
         output_name='docs/manual.md',
         delete_html_comments=True,
         do_full_readme=True)

    log_obj.printout_all()


# def compile_readme():

#     log_obj = BESTLOG()

#     main(logger=log_obj,
#          main_md_file='docs_autogen/readme/markdown_source_files/2_readme.md',
#          insert_md_section_for__class_methods=insert_md_section_for__class_methods,
#          remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
#          output_name='testdocs/readme.md',
#          delete_html_comments=True,
#          do_full_readme=False)

#     log_obj.printout_all()


if __name__ == "__main__":
    # compile_readme()
    compile_index()