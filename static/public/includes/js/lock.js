function lockCluster(url) {
  if (confirm('Are you sure you want to Lock this Cluster?')) {
    return window.location = url;
  } else {
    return 0;
  }
}
