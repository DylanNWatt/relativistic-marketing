Test
=====

.. _installation:

Installation
------------

While the long term goal for Relativistic is to provide a stable module api for terraform projects to be able to import, the current version is designed as a boilerplate.

The suggested usage is to fork the repository and modify the code to suit your needs.

Assuming you have the github CLI installed, you can run the following command to create a new repository from the template:
.. code-block:: console

   $ gh repo fork kadreio/relativistic

Deploying Locally
----------------

Relativistic's purpose can be summed up as "you give us a kubernetes cluster, and we'll give you a data stack." It does not concern itself with the actual creation of that cluster.

As such, you'll need to create a kubernetes cluster for local development. There are several projects out that that do this.

As recommendations, but not requirements:

- For Linux: [Minikube](https://minikube.sigs.k8s.io/docs/)
- For Mac: Docker For Mac's [Built in Kubernetes](https://www.docker.com/blog/docker-mac-kubernetes/)

.. .. autofunction:: lumache.get_random_ingredients

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
.. will raise an exception.

.. .. autoexception:: lumache.InvalidKindError

.. For example:

.. >>> import lumache
.. >>> lumache.get_random_ingredients()
.. ['shells', 'gorgonzola', 'parsley']

