import multiprocessing
import numpy as np

class KMeansMapper(multiprocessing.Process):
    def __init__(self, data_chunk, centroids, result_queue):
        super().__init__()
        self.data_chunk = data_chunk
        self.centroids = centroids
        self.result_queue = result_queue

    def run(self):
        pass
        # TODO: Implement the run method. This method should assign each point in self.data_chunk to the nearest centroid and put the result in the result_queue.
        # The result should be a tuple containing the index of the nearest centroid and the point itself.
        # Process each point in the data chunk
        for point in self.data_chunk:
            # Calculate distances to all centroids
            distances = [np.linalg.norm(point - centroid) for centroid in self.centroids]
            
            # Find the index of the nearest centroid
            nearest_centroid_idx = np.argmin(distances)
            
            # Put the result (centroid index, point) in the queue
            self.result_queue.put((nearest_centroid_idx, point))