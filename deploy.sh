#!/usr/bin/env bash

while [[ "$#" -gt 0 ]]; do case $1 in
  -b|--build) BUILD="1";;
  *) echo "Error, unknown parameter passed: $1."; exit 1;;
esac; shift; done

if [[ ${BUILD} ]]
then
  echo "Building docker images and pushing to docker hub, asking for root access.."
  sudo docker build -t yaqc/tester:v1.1 .
  sudo docker push yaqc/tester:v1.1
fi

kubectl create namespace jobs
kubectl apply -f manifests/serviceaccount.yaml
kubectl apply -f manifests/role.yaml
kubectl apply -f manifests/rolebinding.yaml
kubectl apply -f manifests/pod.yaml