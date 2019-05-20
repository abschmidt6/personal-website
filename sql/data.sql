INSERT INTO projects(pid, title, class, daterange)
VALUES
(1, 'Syetem Design of a Search Engine', 'EECS 398 - 001 (MDE)', 'Upcoming'),
(2,  'This Website', 'Personal Project', 'Ongoing'),
(20, 'Py-Time-Slice', 'Personal Project', 'May 2019'),
(21, 'Computer Forensics', 'EECS 388: Computer Security', 'April 2019'),
(22, 'Wikipedia Search Engine', 'EECS 485: Web Systems', 'April 2019'),
(23, 'Application Security', 'EECS 388: Computer Security', 'March 2019'),
(24, 'Networking and Web Secuirty', 'EECS 388: Computer Security', 'March 2019'),
(25, 'Instagram Clone', 'EECS 485: Web Security', 'February 2019'),
(26, 'Database Design', 'EECS 484: Database Management Systems', 'December 2018'),
(27, 'Citizen Science for the Dark Energy Survey', 'Undergraduate Research', 'May 2018'),
(28, 'Traveling Salesman Problem', 'EECS 281: Data Structures and Algorithms', 'December 2017'),
(29, 'Computer Architecture', 'EECS 370: Introduction to Computer Organization', 'December 2017'),
(30, 'Stock Market Simulation', 'EECS 281: Data Structures and Algorithms', 'November 2017');

INSERT INTO project_action_points(apid, proj_id, bp)
VALUES
(1, 26, 'Build and queried databases using SQL, Java, and MongoDB'),
(2, 26, 'Linear Hashing Index, External Merge Sort, and Grace Hash Join implementations'),
(3, 28, 'Minimum Spanning Tree implementations using Prim’s and Kruskal’s Algorithms'),
(4, 28, 'Approximations using a nearest neighbor algorithm and 2-opt'),
(5, 28, 'Optimal solution implementation using a branch and bound algorithm'),
(6, 29, 'Implemented an assembler, CPU simulator (single-cycle and pipeline), cache simulator'),
(7, 29, 'Translated functions to assembly including integer multiplication and a recursive combination formula'),
(8, 30, 'Implemented a Hash Table and Priority Queue'),
(9, 30, 'Further experience with Stacks, Queues, Pairing Heaps, templated classes'),
(10, 1, 'A semester long project to build a search engine in a group of 6+ students. Details to come...'),
(11, 21, 'Analyze a hard drive and hidden communication networks to determine whether a disgruntled ex-employee''s actions were illegal'),
(12, 21, 'Used live and dead analysis of the hard drive, password crackers, SQL injections, steganalysis, and social engineering to gather evidence'),
(13, 22, 'Search all of Wikipedia with a search engine built off of the hadoop MapReduce pipeline, PageRank scores, and tf-idf scores'),
(14, 22, 'Includes an optional PageRank/tf-idf score weight slider to control the weight of each factor'),
(15, 23, 'Used buffer overflow attacks and ROP gadgets to hijack control of vulnerable programs'),
(16, 23, 'Overwrote return addresses and opened a root shell in simple situations, with DEP enabled, and with variable stack positions'),
(17, 24, 'Used SQL Injections, Cross Site Scripting (XSS), and Cross Site Request Forgery (CSRF) to attack vulnerable websites and gain access to protected data'),
(18, 24, 'Analyzed web traffic with Wireshark to locate vulnerabilities.'),
(19, 25, '3-part project consisting of a static site, server-side dynamic site, and client-side dynamic site all of which are rudamentary copies of Instagram'),
(20, 25, 'Can create or delete users, posts, comments, and likes'),
(21, 25, 'Built using python, flask, jinja2, and sqlite'),
(22, 27, 'Independently programmed image analysis and editing programs to improve photos from cosmological surveys'),
(23, 27, 'Lead image manipulation efforts by filtering images to isolate and enhance the most useful data'),
(24, 20, 'Created a python program to combine a series of hundreds of timelapse images into one composite image'),
(25, 20, 'Built a GUI to make it more user-friendly and handle errors in a better way'),
(26, 20, 'Fully functional and optimized accross a variety of different options'),
(27, 2, 'Development on this website began in March 2019'),
(28, 2, 'Right now this is a server-side dynamic, templated website running a sqlite database');

INSERT INTO project_links(plid, proj_id, link, link_type)
VALUES
(1, 20, '/static/videos/pytimeslice.mp4', 'video'),
(2, 2, 'https://github.com/abschmidt6/personal-website', 'github'),
(3, 20, 'https://github.com/abschmidt6/py-time-slice', 'github');