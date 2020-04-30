import sys
import getopt
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


HOST = ""
PORT = 0
INTERVAL = 0

def stream():
    sc = SparkContext("local[2]", "NetworkWordCount")
    ssc = StreamingContext(sc,INTERVAL)

    lines = ssc.socketTextStream(HOST,PORT)

    words = lines.flatMap(lambda x: x.split(" "))

    pairs = words.map(lambda word: (word,1))
    count = pairs.reduceByKey(lambda x,y: x + y)
    count.pprint(100)

    ssc.start()

    try:
        while(True):
            pass
    except KeyboardInterrupt:
        print("Bye Bye")
        ssc.stop()

def main():
    global HOST, PORT, INTERVAL
    args = sys.argv[1:]
    opts, _ = getopt.getopt(sys.argv[1:], "h:p:i:", ["host=", "port=", "interval="])
    for key, value in opts:
        if key == "-h" or key == "--host":
            HOST = value
        if key == "-p" or key == "--port":
            PORT = int(value)
        if key == "-i" or key == "--interval":
            INTERVAL = int(value)
    stream()


if __name__ == "__main__":
    main()