#!/usr/bin/env bash
set -eu

output=tests/tmp

echo "///////////////////////////////////////////"
echo "             TAGGING TEMPLATE COPY"
echo "///////////////////////////////////////////"
echo
template=$(mktemp -d)
cp -rf . "${template}"
(
  cd "${template}" || exit 1
  git add . -A || true
  git commit -m "test" || true
  git tag 99.99.99
)
echo "Template copy located at ${template}"

echo
echo "///////////////////////////////////////////"
echo "             GENERATING PROJECT"
echo "///////////////////////////////////////////"
echo
copier -f "${template}" "${output}" \
  -d project_name="Test Project" \
  -d project_description="Testing this great template" \
  -d author_fullname="Jean Dupont" \
  -d author_username="jdp" \
  -d author_email="jean@dupo.nt"
cd "${output}"
git init .

echo
echo "///////////////////////////////////////////"
echo "             TESTING PROJECT"
echo "///////////////////////////////////////////"
echo
echo ">>> Creating initial commit (feat)"
git add -A .
git commit -am "feat: Initial commit"
git tag 0.1.0
echo
echo ">>> Setting up project"
make --no-print-directory setup
echo
echo ">>> Running tests"
make --no-print-directory nox-test

echo
echo "///////////////////////////////////////////"
echo "             UPDATING PROJECT"
echo "///////////////////////////////////////////"
echo
copier -f update

echo
echo "///////////////////////////////////////////"
echo "             CLEANUP"
echo "///////////////////////////////////////////"
echo
echo ">>> Removing ${template}"
rm -rf "${template}"
