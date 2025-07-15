from pygifgenerator_testver.gifgenerator import GIFGenerator

g = GIFGenerator(inputPath='./project/images/*.png', outputPath='./project/image_out/result.gif', imgSize=(640, 480))

g.generate_gif()