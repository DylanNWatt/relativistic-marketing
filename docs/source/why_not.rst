Don't Use If
=====

.. _why_not:

You need a stable interface
----------------

The foundational premise that Kubernetes has become a de facto standard for open source projects to provide a production grade deployment is sound, but the best way to administer it is still up for debate.

This project uses terraform + helm to manage deployments. This has limitations where "reconcilitions" can only be made at deploy time. There's been a recent trend of using gitops plus something like ArgoCD to manage deployments. 

This may be the long term direction for Relativistic, but ArgoCD applications will need to be defined for each application.

The goal of a v1.0.0 of Relativistic a non breaking interface going forward. For now, it's a living project that feedback will influence towards the best design.


You don't want to operate your own data stack
----------------
Relativistic is designed to be a self-service project to stand up data infrastructure. It brings the implementation cost of starting a project from scratch down to a few commands, but over time it will have operational costs. You'll need to upgrade kubernetes clusters, make sure SSL certificates are valid, and make sure your databases are backed up.

Many of these things can be automated, and for far less than the cost of a managed service, but you will be responsible for them, not a vendor.


