---
type: notion-import
notion-id: 74199a8c893743e19f33892a245a76d4
source-url: https://app.notion.com/p/lewagon/Data-Science-content-process-74199a8c893743e19f33892a245a76d4
imported: 2026-07-21
---
# Data Science content process
When developing a new track that involves the Data Science material, there are several things to consider. First, it makes sense to step back and ask “What is a Data Science Track?”. This seems like a simple question and the answer is simple:
- It is a track that takes N days to deliver and teach to students
- For every day there must be:
        - A lecture
        - Challenges
        - A recap
- The key consideration for organizing a track must then be:
        - “How do I get the right lecture onto Kitt for lecturers to teach and students to go through?”
        - “How do I get the right challenges onto Kitt so that, when a student runs the download script presented to them on Kitt, the individual challenge clones into the correct place and runs on their computer?”
        - “Can the lecturer access and run the right notebook for the Recap (this functions just like a regular challenge most of the time)?”
The data-meta syllabus.yml files serve as a neat way of organizing all this information into one place and - from this document - Kitt gets assembled. For a Kitt program to be built (or even just tested: see [[How to Preview Content Changes on Kitt|previewing Kitt]] tutorial), a few things are needed:
- A branch on data-meta with its own syllabus.yml to construct each day
- A branch on data-solutions which contains ALL challenges referenced by syllabus.yml
- We typically use the master branch on data-lectures which is messy but it functions as a lake of lectures that we can pull relevant lectures from
- A clear idea of how the course will be deployed to students - NEVER underestimate deployment. I would argue it’s one of the most important pieces of the puzzle and the first thing I do on each track now is prioritize making sure it looks right and deploys right from the students set-up (e.g. using DataStudio’s non-persistent JupyterLab for Air Liquide, using miniconda for IKEA, using GitLab + CACIB’s JupyterLab server for CACIB, or using the conventional WSL Linux set-up that we get Data Science students do on B2C). Changing how a track is deployed changes:
        - READMEs for students depending on how they will tackle challenges. Some commands in challenge instructions won’t work or aren’t relevant (e.g. if a student doesn’t have the Git CLI then there can be no references the the git add, git commit and `git push` commands anywhere in the course (see [this change](https://github.com/lewagon/nbresult/commit/524068774c4dbb60a24c7a1033b49f491a32838b) made to the nbresult package we used to change the prompt that shows up for students after they pass tests in a notebook so that they use the GUI instead)
        - Lectures, depending on what tools they need to use (e.g. Air Liquide did not use the Git CLI but instead the native Jupyter Git GUI)
        - The scripts needed to run on Kitt (see [changes made](https://github.com/lewagon/kitt/pulls?q=is%3Apr+script+air+liquide+is%3Aclosed) to the Kitt Download script for the Air Liquide batch to reflect the fact that we were working without SSH, using the gh package authenticated with a $GH_TOKEN and in a file system where only files within the SageMaker folder persisted. All of these had to be adjusted for in the download script be @Toni Panacek with help from @Gaëtan Manchon)
The easiest way to get started on a track is:
1) Make your data-meta branch (probably from an existing B2B branch e.g. the Air Liquide branch which is the most up-to-date version of the 3 week course with the most content)
2) Make your data-solutions branch (probably from an existing B2B branch e.g. the Air Liquide branch which is the most up-to-date version of the 3 week course with the most content)
3) Set data-lectures branch to be the master branch then test that the lectures render correctly using the Kitt preview function.
4) Once it renders correctly on Kitt, you then need to test that the challenges clone correctly:
- To do this, you need to simulate the student’s experience and behave as a student/ auditor on Kitt (this should be done from the student environment - i.e. from DataStudio or from minconda if you plan to use miniconda). Then ask:
        - Are the challenges downloading correctly/ at all
        - Are they challengified correctly? Does the teacher solution correctly differ from the student solution?
5) Once this all works, then actually start adding challenges, following the workflow provided [here](https://app.notion.com/p/3762036e7c104ea885c9b6c2c672f4cc?pvs=25). It is easier to start working from a wireframe that you know deploys effectively than it is trying to do everything at once. Content is the EASIEST thing to modify/ add once you have everything else working.
6) Ensure all of your added challenges have READMEs, metadata.yml in a .lewagon folder and are correctly challengified. Then ensure that solution paths and linked meta syllabus.yml files all align correctly in the Kitt simulator before approving PRs.
## Related
- [[Content]]
