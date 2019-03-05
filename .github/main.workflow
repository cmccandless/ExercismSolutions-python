workflow "Lint and Test on push" {
  on = "push"
  resolves = ["Python 3.7"]
}

action "Python 3.7" {
  uses = "cmccandless/github-action-python/3.7-alpine@master"
  args = "bash .ci.sh"
}
