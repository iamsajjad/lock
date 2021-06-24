function deleteMaintainer(url) {
  if (confirm('Are you sure you want to delete this Maintainer ?')) {
    return window.location = url;
  } else {
    return 0;
  }
}
