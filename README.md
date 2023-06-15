# Rosalind
Eclipse projects for Rosalind

Rosalind is a platform for learning bioinformatics and programming through problem solving, and has a bias towards using Python to solve the problems (it includes a small Python course, and the utility libraries that are recommended are Python).  Since bioinformatics is text and graph oriented, it's a nice counterpoint to the numeric processing of Euler.  See http://rosalind.info for more info.

This repo holds the Eclipse pydev projects I am using to explore Rosalind, along with getting more familiar with github and egit (git plugin for Eclipse).

- Python Village
  These projects cover the "Python Village" introduction to Python, and are named according to the ID of each problem.  Not much of a tutorial - these are more like exercises to introduce Python concepts that need to be researched elsewhere, and then tested here.  Completing these problems demonstrates a familiarity with Python.

  The structure of each project includes :
  - sample.txt : A file that contains the provided sample data from the problem (usually a small, simple version used as an example), saved as a file that will match the actual problem data that will be downloaded from Rosalind.
  - rosalind_<ID>_#_dataset.txt : <ID> matches the ID of the problem, # is the number of the download (usually "1", but may be multiple if multiple attempts were needed).  A file that contains the actual data for solving the problem - similar to the sample, but usually with more complex/larger/longer data than the example, and thus needs to be processed by a computer (the example data can often nbe solved by hand).
  - results.txt : A file with the answer produced by processing the dataset file.  If the problem specifies a particular format, it will match this format = it is ready to upload as a solution to Rosalind.
  - ###.py : ### is the version of the solution code used to solve the problem.  Often, the problem has an obvious coding solution that is not very efficient - in many cases, this is enough to solve the problem, but problems that deal with efficient algorithms will often require a better algorithm to solve in the allotted time.  In other cases, there may be alternative approaches, and the multiple versions are provided to allow for comparisons between the approaches.

The datasets/results are done as files, because the problems provide the data as a file to be downloaded (the contents change each time), and the results need to be uploaded as a file (the correct results also change each time, to match the provided data) - and these typically need to be downloaded, processed, and uploaded in 5 mins.  Some of the simpler problems allow for pasting in an answer, but this is easily done by opening the file and doing copy/paste - more complex problems require a file to be uploaded, and no copy/paste option is available.  While this is overkill for the simpler problems, it helps a lot in the more complex problems that come down the road.

The actual problem solution code is contained within a "processData" function, which allows for a simple unit test to be done using the sample data and the sample result (included as an assertion in the code).  More sophisticated code can wrap calls with timing information or other metrics to be captured.

The solution includes a comment at the start, desribing the problem (usually copied from the problem on the Rosalind page - including examples).  Note the use of the UTF-8 encoding directive to allow special symbols to be included in the comments, as the problem statements often include math symbols.

Note that INI1 is missing - it's a trivial problem that does not require coding.

- Algorithmic Heights
  The projects implement a number of algorithms.  The focus is on the algorithm, and not the Python code - but implementing these helps build facility in whatever language you are using, so they are a good way to build Python skills.  Since the problem/solution approach is the same as Python Village, the project structure is basically the same.
