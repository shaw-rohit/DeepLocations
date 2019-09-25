## The Task
Crawl the flickr picture archive to get a large amount of pictures with GPS annotations. Now try to train a deep learning model to learn the GPS location of a picture. It could be a good idea to remove persons from the pictures automatically, but you must figure this out for yourselves. Create a visualization that shows the accuracy of your approach and/or allows to upload a picture and predicts its GPS location.

## The Data
```
4571314348      47065077@N00    savagecat       2010-04-16 11:00:49.0   1272811190      Canon+EOS+400D+DIGITAL  On+the+Wall             b%26w,black+%26+white,choir+tour,hadrian%27s+wall,noir+et+blanc,portrait,sewingshields,st+george%27s,wall               -2.335453       55.010991       12      http://www.flickr.com/photos/47065077@N00/4571314348/   http://farm5.staticflickr.com/4036/4571314348_03a71b7bbb.jpg    Attribution License     http://creativecommons.org/licenses/by/2.0/     4036    5       03a71b7bbb      62ffbfb29f      jpg     0
```

1. Photo/video identifier
2. User NSID
3. User nickname
4. Date taken
5. Date uploaded
6. Capture device
7. Title
8. Description
9. User tags (comma-separated)
10. Machine tags (comma-separated)
11. Longitude
12. Latitude
13. Accuracy
14. Photo/video page URL
15. Photo/video download URL
16. License name
17. License URL
18. Photo/video server identifier
19. Photo/video farm identifier
20. Photo/video secret
21. Photo/video secret original
22. Photo/video extension original
23. Photos/video marker (0 = photo, 1 = video)

## The Steps
It would be best to start with a subset of the data/images and expand as progress is made.

1. Transform data
    - Add column headers
2. Clean data
    - Drop unwanted columns
    - Only keep instances with GPS coordinates
3. Download images
4. Implement face recognition
    - Identify all images with faces in them
    - Drop all such instances
5. Develop a deep learning model
    - Train the model based on tags linked to the GPS coordinates
    - Note accuracy and other metrics
    - Improvise wherever possible
6. Test the model
    - With a different subset of images
    - Note accuracy and other metrics
    - Improvise wherever possible
7. Create a fancy visualization
8. Make it to the hall of fame (result showcase)
