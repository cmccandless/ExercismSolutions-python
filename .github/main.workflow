workflow "Lint and Test on push" {
  on = "push"
  resolves = [
    "Python 3.6",
    "Python 3.7",
    "Python 3.8-rc",
  ]
}

action "Python 3.6" {
  uses = "cmccandless/github-action-python/3.6@master"
  args = "bash .ci.sh"
}

action "Python 3.7" {
  uses = "cmccandless/github-action-python/3.7@master"
  args = "bash .ci.sh"
}

action "Python 3.8-rc" {
  uses = "cmccandless/github-action-python/3.8-rc@master"
  args = "bash .ci.sh"
}
