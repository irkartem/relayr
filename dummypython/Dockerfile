FROM python 

# File Author / Maintainer
MAINTAINER Maintaner Name

# Copy the application folder inside the container
ADD ./run.py /run.py

# Expose ports
EXPOSE 8080

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python /run.py
