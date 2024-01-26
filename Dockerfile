FROM pytorch/pytorch:latest
RUN pip install matplotlib scikit-learn
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]

