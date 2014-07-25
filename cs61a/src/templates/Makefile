# All credit for this Makefile goes to Albert Wu
BASE_PATH=~/Sites/personal_website/dicksontsai.github.io/cs61a
REVIEW_PATH=$(BASE_PATH)/review

COMPILER=templar compile -m

INDEX_TEMP=template.html
Q_TEMP=question.html
Q_PY=../python_files/

TOPICS=$(MT1_TOPICS) $(MT2_TOPICS) $(FINAL_TOPICS)

.PHONY: pub-assets all all-mt1 all-mt2 all-final clean

#Make all the problem files
all:
	make index-index
	make all-mt1
	make all-mt2
	make all-final
	make pub-assets

#Checks if we need to create the BASE_PATH and REVIEW_PATH folders
#Shouldn't be necessary unless we change their locations
pub-assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	#The next command is if you want to copy formatting files to the
	# REVIEW_PATH
	#cp -r public $(REVIEW_PATH)
	
all-mt1:
	make index-mt1
	for topic in $(MT1_TOPICS); do \
		if [ -d contents/$$topic ]; then \
			make pub-$$topic
		fi; \
	done

all-mt2:
	make index-mt2
	for topic in $(MT2_TOPICS); do \
		if [ -d contents/$$topic ]; then \
			make pub-$$topic
		fi; \
	done

all-final:
	make index-final
	for topic in $(FINAL_TOPICS); do \
		if [ -d contents/$$topic ]; then \
			make pub-$$topic
		fi; \
	done

index-%: indices/%.md
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	$(COMPILER) -s $(INDEX_TEMP) -d $(REVIEW_PATH)/$*.html

pub-%: contents/%
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	# Recreate whatever's in the review_path directory
	if [ -d $(REVIEW_PATH)/$* ]; then rm -rf $(REVIEW_PATH)/$*; fi
	mkdir $(REVIEW_PATH)/$*
	# Different markdowns for different difficulties
	if [ -f $</basic.md ]; then \
		$(COMPILER) -s $</basic.md $(Q_TEMP) -d $(REVIEW_PATH)/$*/basic.html; fi
	if [ -f $</exam.md ]; then \
		$(COMPILER) -s $</exam.md $(Q_TEMP) -d $(REVIEW_PATH)/$*/exam.html; fi
	if [ -d $</assets/ ]; then \
		cp $</assets/* $(REVIEW_PATH)/$*/ ; fi

$(TOPICS):
	if [ -d contents/$@ ]; then rm -rf contents/$@; fi
	mkdir contents/$@ contents/$@/basic contents/$@/exam contents/$@/basic/assets contents/$@/exam/assets
	cp $(Q_PY) contents/$@/basic.md
	cp $(Q_PY) contents/$@/exam.md
